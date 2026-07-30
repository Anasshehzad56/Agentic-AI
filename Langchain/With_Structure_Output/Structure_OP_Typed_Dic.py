from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Scheema 

class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke(""" The iPhone 14 Pro remains a highly capable and premium device. It stands out for its bright 120Hz display, innovative Dynamic Island, and exceptional triple-lens camera, which brought a massive 48MP main sensor to the lineup. However, its hefty stainless steel build and reliance on the legacy Lightning port are notable drawbacks.  """)

print(result)