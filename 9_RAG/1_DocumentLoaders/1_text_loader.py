from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model='gpt-5.4-mini', temperature=0)
parser = StrOutputParser()

loader = TextLoader(
    "/Users/pradyumnareddy/GenAI/9_RAG/1_DocumentLoaders/cricket.txt",
    encoding="utf-8"
)

docs = loader.load()

prompt = PromptTemplate(
    template="Write a summary of the following poem\n {poem}",
    input_variables=['poem']
)

chain = prompt | model | parser

result = chain.invoke({'poem': docs[0].page_content})

print(result)