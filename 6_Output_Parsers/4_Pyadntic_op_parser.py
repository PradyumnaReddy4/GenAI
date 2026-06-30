from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model='gpt-5.4', temperature=0)

class Person(BaseModel):
    name: str = Field(description="name of the person")
    age: int = Field(gt=18, description="Age of the person")
    city: str = Field(description="Name of the city student belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='tell me about {name}\n {format_instruction}',
    input_variables=['name'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'name': 'tim cook'})

print(result)