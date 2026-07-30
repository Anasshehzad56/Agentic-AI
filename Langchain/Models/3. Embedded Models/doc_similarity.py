from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

model = GoogleGenerativeAIEmbeddings(
     model="models/gemini-embedding-001",
    output_dimensionality=32  )

documents = [
    "Babar Azam is a Pakistani cricketer known for his elegant batting and leadership.",
    "Sarfaraz Ahmed is a former Pakistani captain famous for his calm demeanor and finishing skills.",
    "Javed Miandad, also known as the 'King of Match-Winning Knocks', holds many batting records.",
    "Fakhar Zaman is known for his aggressive batting and record-breaking double centuries.",
    "Shaheen Afridi is a Pakistani fast bowler known for his unorthodox action and yorkers."
]

query = "Tell me About Babar Azam"

doc_embeddings = model.embed_documents(documents)


query_embedding = model.embed_query(query)

# To find similarity score 
# print(cosine_similarity([query_embedding], doc_embeddings))

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

#Added index to each score
index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(query)
print(documents[index])


