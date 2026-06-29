from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

prompts = ChatPromptTemplate([
    ('system', 'you are a helpful ecommerce agent to help customers'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

chat_historys = []

with open('/Users/pradyumnareddy/GenAI/4_LANGCHAIN_PROMPTS/chat_history.txt', 'r') as f:
    chat_historys.extend(f.readlines())

ans = prompts.invoke({'chat_history': chat_historys,'query': 'where is my refund'})

model = ChatOpenAI(model='gpt-5.4-mini', temperature=0.5)

answer = model.invoke(ans)

print(answer.content)