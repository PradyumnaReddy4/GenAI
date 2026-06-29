from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-5.4-mini", temperature=0)

chat_history = [
    SystemMessage(content="You are a helpful AI Assistant help me with my querys")
]

while(True):
    user_input = input("User: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result))
    print("Ai: ", result.content)
print(chat_history)