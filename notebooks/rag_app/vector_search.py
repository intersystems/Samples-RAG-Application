import os

import intersystems_iris.dbapi._DBAPI as iris

from dotenv import find_dotenv, load_dotenv

class VectorSearch:
    def __init__(
        self,
        host: str | None = None,
        port: int | None = None,
        namespace: str | None = None,
        username: str | None = None,
        password: str | None = None,
    ) -> None:
        load_dotenv(find_dotenv(usecwd=True), override=True)

        resolved_host = host or os.getenv("IRIS_HOST", "localhost")
        resolved_port = int(port or os.getenv("IRIS_PORT", "51972"))
        resolved_namespace = namespace or os.getenv("IRIS_NAMESPACE", "USER")
        resolved_username = username or os.getenv("IRIS_USERNAME", "SuperUser")
        resolved_password = password or os.getenv("IRIS_PASSWORD")

        if not resolved_password:
            raise ValueError("IRIS_PASSWORD is not set (set it in your environment or .env)")

        self.conn = iris.connect(
            resolved_host,
            resolved_port,
            resolved_namespace,
            resolved_username,
            resolved_password,
        )
        
    def search_by_q_and_a(self, query_embedding, top_k:int=4) -> list:
        query = f"""SELECT TOP {top_k} data.Story, data.ID
                    FROM RAG_COQA.Story data
                    JOIN RAG_COQA.QandA vector
                    ON vector.StoryID = data.ID
                    ORDER BY VECTOR_DOT_PRODUCT(TO_VECTOR(vector.QuestionEmbedding), TO_VECTOR(?)) DESC
                    """
        iris_cursor = self.conn.cursor()
        iris_cursor.execute(query, [str(query_embedding)])
        origin_list = iris_cursor.fetchall()
        return origin_list
    
    def search_by_story(self, query_embedding, top_k:int=2) -> list:
        query = f"""SELECT TOP {top_k} data.Story, data.ID
                    FROM RAG_COQA.Story data
                    ORDER BY VECTOR_DOT_PRODUCT(TO_VECTOR(data.StoryEmbedding), TO_VECTOR(?)) DESC
                    """
        iris_cursor = self.conn.cursor()
        iris_cursor.execute(query, [str(query_embedding)])
        origin_list = iris_cursor.fetchall()
        return origin_list
    
    def search_q_and_a_docs_by_story(self, story_ids: list[str], top_k:int=1) -> list:
        id_tuple = tuple(story_ids)
        print(id_tuple)
        query = f"""SELECT TOP {top_k} Question, Answer
                    FROM RAG_COQA.QandA
                    WHERE StoryID IN {id_tuple}
                    """
        iris_cursor = self.conn.cursor()
        iris_cursor.execute(query)
        resultset = list(iris_cursor.fetchall())
        q_and_a_list = [{'question':q_and_a[0], 'answer':q_and_a[1]} for q_and_a in resultset]
        return q_and_a_list
    
    