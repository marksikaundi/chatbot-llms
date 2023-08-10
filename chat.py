from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain

chat = ChatOpenAI(openai_api_key="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")


# chat = ChatOpenAI()
chat([HumanMessage(content="Translate this sentence from English to French: I love programming.")])

messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="I love programming.")
]
chat(messages)

AIMessage(content="J'adore la programmation.", additional_kwargs={}, example=False)
conversation = ConversationChain(llm=chat)  
conversation.run("Translate this sentence from English to French: I love programming.")

conversation.run("Translate it to German.")