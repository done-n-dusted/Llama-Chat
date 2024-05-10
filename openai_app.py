from langchain import OpenAI
from langchain import ConversationChain

import os
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.7)

conversation = ConversationChain(llm=llm)

answer = conversation.predict(input="Hi there!")

while True:
    print("AI:", answer)
    print()
    print("Type 'quit' to exit the chat.")
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    answer = conversation.predict(input=user_input)