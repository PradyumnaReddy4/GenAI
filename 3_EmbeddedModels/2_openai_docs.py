from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

docs = ["Virat is a Cricketer", "Ronaldo is a foorballer", "Jordan is a basketball player"]

model = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=6)

result = model.embed_documents(docs)

print(str(result))