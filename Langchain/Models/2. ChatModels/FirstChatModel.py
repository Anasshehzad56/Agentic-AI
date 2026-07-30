from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

ChatModel = ChatGoogleGenerativeAI( model="gemini-2.5-flash",  temperature=0.7,
    max_output_tokens=2500)

result = ChatModel.invoke("Who is Virat Kohli")

print(result.content)