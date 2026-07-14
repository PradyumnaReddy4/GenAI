from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-5.4', temperature=0)

parser = StrOutputParser()

template1 = PromptTemplate(
    template="Explain the {topic} with all main points",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Explain in depth about this {text}',
    input_variables=['text']
)

chain = template1 | model | parser | template2 | model | parser

chain.get_graph().print_ascii()

result = chain.invoke({'topic': 'trump'})

print(result)
