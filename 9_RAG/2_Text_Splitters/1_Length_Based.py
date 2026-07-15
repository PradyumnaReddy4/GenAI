from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

path = "/Users/pradyumnareddy/GenAI/9_RAG/1_DocumentLoaders/dl-curriculum.pdf"

loader = PyPDFLoader(path)

splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 20,
    separator = ""
)

docs = loader.load()

result = splitter.split_documents(docs)

print(result[2].page_content)