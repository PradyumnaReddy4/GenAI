from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model='gpt-5.4-mini', temperature=0)

template1 = PromptTemplate(
    template="Write a detailed Report on the following {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="Write a 5 line summary on the text given {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic': 'BlackHole'})

print(result)
