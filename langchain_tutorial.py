from secret import OPENAI_API_KEY, GROQ_API_KEY, GROQ_MODEL,OPENAI_MODEL
from langchain_groq import ChatGroq
from langchain.chat_models import init_chat_model

llm = ChatGroq(api_key=GROQ_API_KEY,model=GROQ_MODEL)
llms = init_chat_model(model=OPENAI_MODEL)

response = llm.invoke("What is the capital of France?")
print(response.content)

