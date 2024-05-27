import dspy

examples = [
    dspy.Example(
        question="What is the capital of France?",
        answer="Paris",
        context="France is a country located in Western Europe. Its capital and largest city is Paris, known for its iconic landmarks like the Eiffel Tower, Notre-Dame Cathedral, and the Louvre Museum."
    ),
    dspy.Example(
        question="Who wrote the novel 'To Kill a Mockingbird'?",
        answer="Harper Lee",
        context="To Kill a Mockingbird is a classic novel written by American author Harper Lee, published in 1960. The book is set in the 1930s in the fictional town of Maycomb, Alabama, and follows the story of a young girl named Scout and her family."
    ),
    dspy.Example(
        question="What is the largest ocean on Earth?",
        answer="Pacific Ocean",
        context="The Pacific Ocean is the largest and deepest of the world's five oceans. It covers an area of about 63 million square miles and is located between the continents of Asia and Australia on the west, North and South America on the east, and the Arctic Ocean to the north."
    ),
    dspy.Example(
        question="Who painted the Mona Lisa?",
        answer="Leonardo da Vinci",
        context="The Mona Lisa is a famous painting created by the Italian Renaissance artist Leonardo da Vinci. It is a portrait of a woman, believed to be Lisa del Giocondo, and is one of the most recognizable and studied works of art in the world."
    ),
    dspy.Example(
        question="What is the tallest mountain in the world?",
        answer="Mount Everest",
        context="Mount Everest is the highest mountain in the world, located on the border between Nepal and Tibet (China). It stands at an elevation of 29,032 feet (8,849 meters) above sea level, making it the highest point on Earth's surface."
    ),
    dspy.Example(
        question="Who is the current president of the United States?",
        answer="Joe Biden",
        context="Joe Biden is the 46th and current president of the United States, having assumed office on January 20, 2021. He previously served as the 47th vice president under President Barack Obama from 2009 to 2017."
    ),
    dspy.Example(
        question="What is the chemical symbol for gold?",
        answer="Au",
        context="Gold is a chemical element with the symbol Au (from the Latin word 'aurum') and atomic number 79. It is a dense, soft, shiny, and malleable metal that has been valued for centuries for its beauty and rarity."
    ),
    dspy.Example(
        question="Who invented the telephone?",
        answer="Alexander Graham Bell",
        context="The telephone was invented by Alexander Graham Bell, a Scottish-born American inventor and scientist. Bell is credited with the first successful demonstration of the telephone in 1876, which revolutionized long-distance communication."
    ),
    dspy.Example(
        question="What is the largest planet in our solar system?",
        answer="Jupiter",
        context="Jupiter is the largest planet in our solar system, with a diameter of approximately 139,822 kilometers (86,881 miles). It is a gas giant, composed primarily of hydrogen and helium, and is known for its iconic Great Red Spot, a massive storm larger than Earth."
    ),
    dspy.Example(
        question="Who is the author of the 'Harry Potter' book series?",
        answer="J.K. Rowling",
        context="The 'Harry Potter' book series was written by British author J.K. Rowling. The series follows the adventures of the young wizard Harry Potter and his friends as they navigate the wizarding world and face the dark wizard Lord Voldemort."
    ),
    dspy.Example(
        question="What is the largest mammal in the world?",
        answer="Blue Whale",
        context="The blue whale is the largest mammal on Earth, with an average length of 80-100 feet (24-30 meters) and a weight of up to 200 metric tons. These massive marine mammals are found in all major oceans and are known for their distinctive blue-gray coloration and powerful, low-frequency vocalizations."
    ),
    dspy.Example(
        question="Who is the founder of Apple Inc.?",
        answer="Steve Jobs",
        context="Steve Jobs was the co-founder and former CEO of Apple Inc., the multinational technology company known for its innovative products such as the iPhone, iPad, and Macintosh computers. Jobs, along with Steve Wozniak, founded Apple in 1976 and played a pivotal role in shaping the company's success."
    ),
    dspy.Example(
        question="What is the largest river in the world?",
        answer="Nile River",
        context="The Nile River is the longest river in the world, stretching approximately 6,650 kilometers (4,130 miles) from its source in Burundi to the Mediterranean Sea. The Nile flows through 11 countries in northeastern Africa and has been a vital resource for ancient and modern civilizations in the region."
    ),
    dspy.Example(
        question="Who is the current Prime Minister of the United Kingdom?",
        answer="Rishi Sunak",
        context="Rishi Sunak is the current Prime Minister of the United Kingdom, having assumed office in October 2022. He is the leader of the Conservative Party and the youngest UK Prime Minister in over 200 years."
    ),
    dspy.Example(
        question="What is the chemical symbol for sodium?",
        answer="Na",
        context="Sodium is a chemical element with the symbol Na (from the Latin word 'natrium'). It is a soft, silvery-white, highly reactive metal that is found in many compounds, including table salt (sodium chloride)."
    ),
    dspy.Example(
        question="Who is the inventor of the theory of relativity?",
        answer="Albert Einstein",
        context="Albert Einstein was a German-born theoretical physicist who developed the theory of relativity, one of the two pillars of modern physics. His famous equation, E=mc^2, describes the relationship between energy, mass, and the speed of light, and is one of the most well-known scientific formulas in the world."
    ),
    dspy.Example(
        question="What is the largest continent in the world?",
        answer="Asia",
        context="Asia is the largest continent in the world, covering an area of approximately 44.58 million square kilometers (17.21 million square miles). It is the most populous continent, home to over 4.7 billion people, and is known for its diverse cultures, landscapes, and economies."
    ),
    dspy.Example(
        question="Who is the author of the 'Lord of the Rings' book series?",
        answer="J.R.R. Tolkien",
        context="The 'Lord of the Rings' book series was written by the British author J.R.R. Tolkien. The epic fantasy novels, set in the fictional world of Middle-earth, follow the adventures of the hobbit Frodo Baggins and his companions as they attempt to destroy the powerful One Ring and defeat the dark lord Sauron."
    ),
    dspy.Example(
        question="What is the largest bone in the human body?",
        answer="Femur",
        context="The femur is the largest and strongest bone in the human body. It is the thigh bone, located in the upper leg, and is responsible for supporting the weight of the body and facilitating movement."
    ),
    dspy.Example(
        question="Who is the current Pope?",
        answer="Pope Francis",
        context="Pope Francis is the current and 266th Pope of the Catholic Church. He was elected in 2013 and is the first Jesuit pope, as well as the first pope from the Americas."
    ),
    dspy.Example(
        question="What is the chemical symbol for iron?",
        answer="Fe",
        context="Iron is a chemical element with the symbol Fe (from the Latin word 'ferrum'). It is a hard, silvery-gray metal that is essential for many biological processes and is a key component in the production of steel, one of the most widely used materials in the world."
    ),
    dspy.Example(
        question="Who is the founder of Microsoft?",
        answer="Bill Gates",
        context="Bill Gates is the co-founder and former CEO of Microsoft, the multinational technology company that developed the Windows operating system and a wide range of software and hardware products. Gates, along with Paul Allen, founded Microsoft in 1975 and played a pivotal role in the personal computer revolution."
    ),
    dspy.Example(
        question="What is the largest ocean in the world?",
        answer="Pacific Ocean",
        context="The Pacific Ocean is the largest and deepest of the world's five oceans, covering an area of about 63 million square miles (163 million square kilometers). It is bounded by the continents of Asia and Australia to the west, North and South America to the east, and the Arctic Ocean to the north."
    ),
    dspy.Example(
        question="Who is the author of the 'Game of Thrones' book series?",
        answer="George R.R. Martin",
        context="The 'A Song of Ice and Fire' book series, which includes the popular 'Game of Thrones' novels, was written by American author George R.R. Martin. The epic fantasy novels, set in the fictional continent of Westeros, have been adapted into a highly successful HBO television series."
    ),
    dspy.Example(
        question="What is the largest mammal in the African continent?",
        answer="African Elephant",
        context="The African elephant is the largest mammal on the African continent and the largest living terrestrial animal. These massive herbivores can weigh up to 6 tons and are known for their distinctive large ears and long, curved tusks made of ivory."
    ),
    dspy.Example(
        question="Who is the current CEO of Amazon?",
        answer="Andy Jassy",
        context="Andy Jassy is the current CEO of Amazon, the multinational technology company that started as an online bookstore and has since expanded into e-commerce, cloud computing, digital streaming, and various other industries. Jassy succeeded Jeff Bezos as Amazon's CEO in 2021."
    ),
    dspy.Example(
        question="What is the chemical symbol for helium?",
        answer="He",
        context="Helium is a chemical element with the symbol He (from the Greek word 'helios', meaning 'sun'). It is a colorless, odorless, and non-flammable gas that is the second-lightest element in the periodic table, after hydrogen."
    ),
    dspy.Example(
        question="Who is the inventor of the telephone?",
        answer="Alexander Graham Bell",
        context="Alexander Graham Bell was a Scottish-born American inventor and scientist who is credited with the invention of the telephone. In 1876, he made the first successful demonstration of the telephone, which revolutionized long-distance communication and paved the way for modern telecommunications."
    ),
    dspy.Example(
        question="What is the largest desert in the world?",
        answer="Sahara Desert",
        context="The Sahara Desert is the largest hot desert in the world, covering an area of about 3.6 million square miles (9.2 million square kilometers) across North Africa. It is known for its vast expanses of sand dunes, rocky landscapes, and sparse vegetation, and is one of the harshest and most inhospitable environments on Earth."
    ),
    dspy.Example(
        question="Who is the author of the 'Sherlock Holmes' book series?",
        answer="Arthur Conan Doyle",
        context="The 'Sherlock Holmes' book series was created by the British author Sir Arthur Conan Doyle. The series follows the adventures of the brilliant detective Sherlock Holmes and his loyal companion, Dr. John Watson, as they solve various crimes and mysteries in late 19th-century London."
    ),
    dspy.Example(
        question="What is the largest bird in the world?",
        answer="Ostrich",
        context="The ostrich is the largest living bird in the world. These flightless birds can reach heights of up to 9 feet (2.7 meters) and weigh up to 320 pounds (145 kilograms). Ostriches are native to the savannas and deserts of Africa and are known for their distinctive long necks, powerful legs, and ability to run at high speeds."
    ),
    dspy.Example(
        question="Who is the current President of China?",
        answer="Xi Jinping",
        context="Xi Jinping is the current President of the People's Republic of China, having assumed office in 2013. He is also the General Secretary of the Chinese Communist Party and the Chairman of the Central Military Commission, making him the paramount leader of China."
    ),
    dspy.Example(
        question="What is the chemical symbol for silver?",
        answer="Ag",
        context="Silver is a chemical element with the symbol Ag (from the Latin word 'argentum'). It is a soft, lustrous, and highly reflective metal that has been valued for centuries for its beauty, durability, and various industrial and medical applications."
    ),
    dspy.Example(
        question="Who is the inventor of the light bulb?",
        answer="Thomas Edison",
        context="Thomas Edison was an American inventor and businessman who is credited with the invention of the first practical incandescent light bulb. His work on the light bulb, along with numerous other inventions, earned him the nickname 'The Wizard of Menlo Park' and cemented his place as one of the most prolific inventors in history."
    ),
    dspy.Example(
        question="What is the largest country in the world by land area?",
        answer="Russia",
        context="Russia is the largest country in the world by total land area, covering an area of approximately 6.6 million square miles (17 million square kilometers). It spans 11 time zones and is the world's largest country, stretching from the Baltic Sea in the west to the Pacific Ocean in the east."
    ),
    dspy.Example(
        question="Who is the author of the 'Dune' book series?",
        answer="Frank Herbert",
        context="The 'Dune' book series was created by the American science fiction author Frank Herbert. The series, set in a distant future where noble families control the galaxy, is considered one of the most influential and acclaimed works of science fiction literature."
    ),
    dspy.Example(
        question="What is the largest mammal in the ocean?",
        answer="Blue Whale",
        context="The blue whale is the largest mammal in the ocean and the largest animal on Earth. These massive marine mammals can grow up to 100 feet (30 meters) in length and weigh up to 200 metric tons. Blue whales are found in all major oceans and are known for their distinctive blue-gray coloration and powerful, low-frequency vocalizations."
    ),
    dspy.Example(
        question="Who is the current Chancellor of Germany?",
        answer="Olaf Scholz",
        context="Olaf Scholz is the current Chancellor of Germany, having assumed office in 2021. He is a member of the Social Democratic Party of Germany and is the head of the federal government, leading a coalition of three political parties."
    ),
    dspy.Example(
        question="What is the chemical symbol for copper?",
        answer="Cu",
        context="Copper is a chemical element with the symbol Cu (from the Latin word 'cuprum'). It is a reddish-orange, ductile, and malleable metal that has been used by humans for thousands of years in various applications, including electrical wiring, plumbing, and the production of alloys like brass and bronze."
    ),
    dspy.Example(
        question="Who is the inventor of the steam engine?",
        answer="James Watt",
        context="James Watt was a Scottish inventor and mechanical engineer who is credited with the invention of the modern steam engine. His improvements to the steam engine design in the late 18th century played a crucial role in the Industrial Revolution and the development of various industries."
    )
]