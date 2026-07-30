from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation",
    provider="hf-inference"
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of Pakistan?")

print(response.content)