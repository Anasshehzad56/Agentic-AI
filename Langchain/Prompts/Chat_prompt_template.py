from langchain_core.prompts import ChatPromptTemplate





chat_template = ChatPromptTemplate ([
    ('system', 'You are a helpful {domain} Assistant'),
    ('human', 'What is {topic}')

    
])



result = chat_template.invoke({'domain':'cricket','topic':'super over'})
print(result)