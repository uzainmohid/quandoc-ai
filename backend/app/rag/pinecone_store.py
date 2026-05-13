import os

from dotenv import load_dotenv

from pinecone import Pinecone

from langchain_pinecone import PineconeVectorStore

from langchain_ollama import OllamaEmbeddings

load_dotenv()

PINECONE_API_KEY = os.getenv(
    "PINECONE_API_KEY"
)

INDEX_NAME = os.getenv(
    "PINECONE_INDEX"
)

pc = Pinecone(
    api_key=PINECONE_API_KEY
)

index = pc.Index(INDEX_NAME)

print("PINECONE CONNECTED SUCCESSFULLY")


embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


def get_vectorstore():

    vectorstore = PineconeVectorStore(
        index=index,
        embedding=embeddings,
        text_key="text"
    )

    return vectorstore