from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers.structured import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatOpenAI(model='gpt-5.4-mini', temperature=0)

schema = [
    ResponseSchema(name='Fact-1', description='Fact 1 about the topic'),
    ResponseSchema(name='Fact-2', description='Fact 2 about the topic'),
    ResponseSchema(name='Fact-1', description='Fact 1 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Tell me 3 facts about the {topic}\n {instructer}",
    input_variables=['topic'],
    partial_variables={'instructer': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic': 'Kings landing'})

print(result)