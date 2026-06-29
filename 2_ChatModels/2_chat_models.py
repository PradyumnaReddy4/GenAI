from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model='gpt-5.4-mini', temperature=1.8)

result = llm.invoke("Write a Poem on Peddi movie")

print(result.content)