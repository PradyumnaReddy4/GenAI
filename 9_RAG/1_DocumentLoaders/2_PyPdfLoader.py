from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('/Users/pradyumnareddy/GenAI/9_RAG/1_DocumentLoaders/dl-curriculum.pdf')

docs = loader.load()

print(type(docs))
print(docs[0])