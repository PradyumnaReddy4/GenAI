from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch, RunnableSequence
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser

load_dotenv()

model = ChatOpenAI(model='gpt-5.4-mini', temperature=0)
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Give me a breif Notes on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='summarize the {text} a bit small',
    input_variables=['text']
)

seqchain = RunnableSequence(prompt1, model, parser)

branchchain = RunnableBranch(
    (lambda x: len(x.split())>300, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = seqchain | branchchain

print(final_chain.invoke({'topic': 'AI'}))