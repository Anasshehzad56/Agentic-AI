import google.generativeai as genai

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")


model = genai.GenerativeModel("gemini-2.5-flash")

chat = model.start_chat(history=[])

print("=== Gemini AI Chatbot ===")
print("Type 'exit' to stop\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Chat ended.")
        break

    response = chat.send_message(user)

    print("Bot:", response.text.replace("**", ""))
    