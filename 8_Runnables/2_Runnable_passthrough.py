from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser

load_dotenv()

model = ChatOpenAI(model='gpt-5.4-mini', temperature=0)

class about(BaseModel):
    joke: str = Field(description='the original joke')
    explaination: str = Field(description='Explaination of joke')

parser = PydanticOutputParser(pydantic_object=about)
parser2 = StrOutputParser()

jokegenaration = PromptTemplate(
    template='genarate a joke on {topic}',
    input_variables=['topic']
)

template1 = PromptTemplate(
    template="Explain this {joke}",
    input_variables=['joke']
)

chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explaination': template1 | model | parser2
})

final = jokegenaration | model | parser2 | chain 

print(final.invoke({'topic': 'AI'}))