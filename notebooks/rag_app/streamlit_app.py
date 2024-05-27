import streamlit as st

from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain, ConversationChain
from langchain.chains.conversation.memory import ConversationSummaryMemory
from langchain.callbacks import get_openai_callback
from langchain_text_splitters import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain_iris import IRISVector

from sentence_transformers import SentenceTransformer

from vector_search import VectorSearch

st.header('Vector Search', divider='orange')
model = SentenceTransformer("avsolatorio/GIST-Embedding-v0", cache_folder='..\\notebooks\\huggingface_cache')

llm = ChatOpenAI(
        temperature=0,
        openai_api_key="KEY-ABC-DEF",
        model_name='gpt-3.5-turbo'
    )

# Create chain. We are using Summary Memory for fewer tokens.
conversation_sum = ConversationChain(
    llm=llm,
    memory=ConversationSummaryMemory(llm=llm),
    verbose=True
)

with st.sidebar:
    st.header('Settings', divider='orange')
    choose_embed = st.radio("Choose an embedding model:",("all-MiniLM-L6-v2","avsolatorio/GIST-Embedding-v0","None"),index=1)
    choose_LM = st.radio("Choose a language model:",("gpt-3.5-turbo","None"),index=0)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot that can access your vector stores. What would you like to know?"}
    ]

for msg in st.session_state.messages:
    if msg["role"] == "assistant":
        st.chat_message(msg["role"]).write(msg["content"])
    else:
        st.chat_message(msg["role"]).write(msg["content"].replace("$", "\$"))

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt.replace("$", "\$")) # Escaping '$', otherwise Streamlit can interpret it as Latex

    # Instantiate this custom Python class (vector_search.py) which gives us SQL access to the persisted vector embeddings.
    peristent_DB = VectorSearch()

    with st.chat_message("assistant"):
        #;
        # Encode the user's prompt and find the top-k similar questions in the vector DB.
        embedding = model.encode(prompt)
        documents = peristent_DB.search_by_q_and_a(embedding.tolist(), top_k=2)
        story_direct_doc = peristent_DB.search_by_story(embedding.tolist(), top_k=1)
        doc_content_list, doc_id_list = map(list, zip(*documents))
        doc_list = [Document(page_content=doc_content, metadata={"source": "local"}) for doc_content in doc_content_list]
        #;
        # This can potentially return many large documents, so we should use LangChain to chunk the results:
        text_splitter = CharacterTextSplitter(chunk_size=250, chunk_overlap=0)
        docs = text_splitter.split_documents(doc_list)
        #;
        q_and_a_docs = peristent_DB.search_q_and_a_docs_by_story(doc_id_list)

        relevant_docs = [str(doc.page_content)[:250] for doc in docs]
        relevant_docs.append(story_direct_doc)

        relevant_docs[:3]

        template = f"""
                    Prompt: {prompt}

                    Example Responses: {q_and_a_docs}

                    Relevant Documents: {str(relevant_docs)}

                    You should only make use of the provided Relevant Documents. They are important information belonging to the user, and it is important that any advice you give is grounded in these documents. If the documents are irrelevant to the question, simply state that you do not have the relevant information available in the database.
                """
        resp = conversation_sum(template)

        st.session_state.messages.append({"role": "assistant", "content": resp['response']})
        st.write(resp['response'].replace("$", "\$"))
