from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

dict = DirectoryLoader(
    path="/Users/pradyumnareddy/GenAI/9_RAG/1_DocumentLoaders/Books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = dict.lazy_load()

print(*docs)