from langchain_community.llms import LlamaCpp
from langchain import ConversationChain

llm = LlamaCpp(
    model_path="llama-2-7b-chat.Q2_K.gguf"
)

conversation = ConversationChain(llm=llm)

answer = conversation.predict(input="Hi there!")

while True:
    print("AI:", answer)
    print("Type 'quit' to exit the chat.")
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    answer = conversation.predict(input=user_input)