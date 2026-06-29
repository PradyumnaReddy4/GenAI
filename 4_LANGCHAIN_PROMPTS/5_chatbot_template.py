from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate([
    SystemMessage(content="You are a helpful {domain} expert"),
    HumanMessage(content="Help me to study about {topic}")
])

prompt = template.invoke({'domain': 'cricket', 'topic': 'yorker'})

print(prompt)