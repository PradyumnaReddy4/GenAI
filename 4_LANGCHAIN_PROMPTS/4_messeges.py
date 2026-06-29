from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-5.4-mini", temperature=0.5)

messeges = [
    SystemMessage(content = "You are a helpful ai assistant")
]

query = input(HumanMessage("User: "))
messeges.append(query)

result = model.invoke(query)

print(result)
messeges.append(result)
print(messeges)