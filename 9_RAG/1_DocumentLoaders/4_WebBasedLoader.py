from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model='gpt-5.4-mini', temperature=0)
parser = StrOutputParser()

url = "https://www.apple.com/iphone/"
loader = WebBaseLoader(url)

docs = loader.load()

prompt = PromptTemplate(
    template="Answer this {question} from the given {text}",
    input_variables=['question', 'text']
)

chain = prompt | model | parser

res = chain.invoke({'question': 'What is the costliest product among', 'text': docs})

print(res)