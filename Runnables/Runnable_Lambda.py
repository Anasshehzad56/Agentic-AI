from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough,RunnableLambda

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash" )

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate a joke about {topic} \n',
    input_variables={'topic'}
)

def word_counter(text):
    return len(text.split())



joke_gen_chain = RunnableSequence(prompt1,model,parser)

paralell_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'Word_Counter':RunnableLambda(word_counter)
})

final_chain = RunnableSequence(joke_gen_chain,paralell_chain)

result = final_chain.invoke({'topic':'AI'})

print(result)