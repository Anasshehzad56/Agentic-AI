from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash" )

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate a tweek about topic \n {topic}',
    input_variables={'topic'}
)

prompt2 = PromptTemplate(
    template='Generate a linkedin post about topic \n {topic}',
    input_variables={'topic'}
)

paralell_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1,model,parser),
    'linkedin': RunnableSequence(prompt2,model,parser)
    })

result = paralell_chain.invoke({'topic':'AI'})

print(result)