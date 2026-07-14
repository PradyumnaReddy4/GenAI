from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from typing import Literal
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnableLambda

load_dotenv()

llm = ChatOpenAI(model='gpt-5.4-mini', temperature=0)
parser = StrOutputParser()
parser2 = JsonOutputParser()

template1 = PromptTemplate(
    template="Help me to make a breif {platform} post on {topic}",
    input_variables=['platform', 'topic']
)

template2 = PromptTemplate(
    template='Make a short intresting notes on this {topic1} and {topic2} in {parser}',
    input_variables=['topic1', 'topic2'],
    partial_variables={'parser': parser2.get_format_instructions()}
)

template3 = PromptTemplate(
    template="Help me to make a breif {platform} post on {topic}",
    input_variables=['platform', 'topic']
)

mapper = RunnableLambda(
    lambda x: {
        "topic1": x["platform1"],
        "topic2": x["platform2"],
    }
)


chain = RunnableSequence(template1, llm, parser, template2, llm, parser)

parellel = RunnableParallel({
    'platform1': template1 | llm | parser,
    'platform2': template3 | llm | parser
})

final = parellel | mapper | template2 | llm

print(final.invoke({'platform': 'X', 'topic': 'AI'}))