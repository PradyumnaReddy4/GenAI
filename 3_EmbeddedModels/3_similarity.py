from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

docs = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

model = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=6)
query = "Tell me about Bumrah"

res1 = model.embed_documents(docs)
res2 = model.embed_query(query)

result = cosine_similarity(res1, [res2])

index, similarity = sorted(list(enumerate(result)), key=lambda x:x[1])[-1]

print(docs[index])
print(f"with a similarity score of {similarity}")