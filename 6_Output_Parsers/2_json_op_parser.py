from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatOpenAI(model='gpt-5.4-mini', temperature=0)

parser = JsonOutputParser()

template1 = PromptTemplate(
    template='Explain about the topic of {topic} by sections\n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template1 | model | parser

result = chain.invoke({'topic': 'Rakesh Master'})

print(result)
print(type(result))