from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser

load_dotenv()

model = ChatOpenAI(model='gpt-5.4-mini', temperature=0)
parser = StrOutputParser()

def word_count(text):
    return len(text.split())

template = PromptTemplate(
    template="Write a joke on {topic}",
    input_variables=['topic']
)

seqchain = template | model | parser
parchain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word count': RunnableLambda(word_count)
})
final = seqchain | parchain

print(final.invoke({'topic': 'ML'}))