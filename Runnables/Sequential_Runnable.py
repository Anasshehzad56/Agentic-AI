from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash" )

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Give me five facts about topic \n {topic}',
    input_variables={'topic'}
)

chain = RunnableSequence(prompt, model, parser)

result = chain.invoke({'topic':'cricket'})

print(result)

