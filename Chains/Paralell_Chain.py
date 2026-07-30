from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(  model="gemini-2.5-flash" )
parser = StrOutputParser()

promp1 = PromptTemplate(
    template='Generate a short and simmple notes from text \n {text}',
    input_variables=['text']
)

promp2 = PromptTemplate(
    template='Generate 5 short questions from text \n {text}',
    input_variables=['text']
)

promp3 = PromptTemplate(
    template='Merg the provided notes and quiz \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes','quiz']
)

Paralell_chain = RunnableParallel({
    'notes': promp1 | model | parser,
    'quiz': promp2 | model | parser
    })

merg_chain = promp3 | model | parser

text ="""Artificial Intelligence (AI) is a branch of computer science that focuses on creating machines and software capable of performing tasks that normally require human intelligence. These tasks include learning from data, solving problems, understanding natural language, recognizing images, making decisions, and predicting outcomes. AI systems use techniques such as machine learning, deep learning, and natural language processing to improve their performance over time.

AI has become an important part of everyday life. It is used in virtual assistants like Siri and Google Assistant, recommendation systems on Netflix and YouTube, self-driving vehicles, healthcare for disease diagnosis, banking for fraud detection, and customer support through chatbots. Businesses also use AI to automate repetitive tasks, improve productivity, and make data-driven decisions.

Despite its many benefits, AI also presents challenges such as privacy concerns, job displacement due to automation, and ethical issues related to bias and decision-making. Therefore, AI should be developed and used responsibly.

In conclusion, Artificial Intelligence is transforming the way people live and work. As technology continues to advance, AI is expected to play an even greater role in solving complex problems and improving the quality of life across different industries."""

chain =  Paralell_chain | merg_chain

result = chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()