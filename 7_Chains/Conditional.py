from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableLambda
from dotenv import load_dotenv
from typing import Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI(model="gpt-5.4-mini", temperature=0)

class Sentiment(BaseModel):
    sentiment: Literal['Positive', 'Negitive'] = Field(description="How is the product is it +ve or -ve")

parser1 = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Sentiment)

prompt1 = PromptTemplate(
    template="How is the product is it good or bad by this review {text}\n {format}",
    input_variables=['text'],
    partial_variables={'format': parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template="Write a appropriate response for this +ve Review {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="Write a appropriate response for this -ve review {text}",
    input_variables=['text']
)

conditional_chain = RunnableBranch(
    (lambda x: x.sentiment == 'Positive', prompt2 | model | parser1),
    (lambda x: x.sentiment == 'Negitive', prompt3 | model | parser1),
    RunnableLambda(lambda x: "Could not find sentiment")
)

basic_chain = prompt1 | model | parser2

final_chain = basic_chain | conditional_chain

result = final_chain.invoke({'text': 'This is a beautiful phone'})

print(result)

final_chain.get_graph().print_ascii()