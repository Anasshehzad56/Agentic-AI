from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


promt1 = PromptTemplate(
    template = 'Generate a detail report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='give me 5 point summary of the following {text}',
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(  model="gemini-2.5-flash" )

parser = StrOutputParser()

chain = promt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'drugs'})


print(result)

chain.get_graph().print_ascii()
