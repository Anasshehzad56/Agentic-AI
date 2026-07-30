from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda

load_dotenv()
model = ChatGoogleGenerativeAI(  model="gemini-2.5-flash" )

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative both negative or positive dhould be in small alphabets \n {feedback}",
    input_variables=['feedback']

)

feedback = "The product is highly recommended"

classifier_chain = prompt1 | model | parser

prompt2 = PromptTemplate(
    template="Write and  appropiate response to this positive feedback in one sentence  \n {feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template="Write and  appropiate response to this negatice feedback in one sentence  \n {feedback}",
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (
        lambda x: x == "positive",
        prompt2 | model | parser,
    ),
    (
        lambda x: x == "negative",
        prompt3 | model | parser,
    ),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain



result = chain.invoke({'feedback':feedback})

print(result)