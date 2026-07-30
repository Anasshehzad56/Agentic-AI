from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Fixed: Updated the deprecated model to the active gemini-embedding-001
model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    output_dimensionality=32  # You can keep this at 256, 768, or remove it for 3072
)

result = model.embed_query(
    "Islamabad is the Capital of Pakistan"
)

print(str(result))