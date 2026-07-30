from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model = GoogleGenerativeAI(
    model="gemini-2.5-flash")

messages = [
    SystemMessage ( content = "You are a helpful Assistant"),
    HumanMessage (content = "Tell me about Langchain")
]

result = model.invoke(messages)

AIMessage(content = result)
messages.append(AIMessage)

print (messages)
