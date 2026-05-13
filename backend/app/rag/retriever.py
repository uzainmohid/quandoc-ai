# from langchain_community.embeddings import OllamaEmbeddings
# from langchain_community.vectorstores import Chroma

# CHROMA_DB_DIR = "chroma_db"

# embedding_model = OllamaEmbeddings(
#     model="nomic-embed-text"
# )


# def get_retriever():

#     vector_db = Chroma(
#         persist_directory=CHROMA_DB_DIR,
#         embedding_function=embedding_model
#     )

#     retriever = vector_db.as_retriever(
#         search_kwargs={"k": 4}
#     )

#     return retriever 

# from langchain_community.embeddings import OllamaEmbeddings
# from langchain_community.vectorstores import Chroma

# CHROMA_DB_DIR = "chroma_db"

# embedding_model = OllamaEmbeddings(
#     model="nomic-embed-text"
# )


# def get_retriever():

#     vector_db = Chroma(
#         persist_directory=CHROMA_DB_DIR,
#         embedding_function=embedding_model,
#         collection_name="harvey_ai_docs"
#     )

#     retriever = vector_db.as_retriever(
#         search_type="similarity",
#         search_kwargs={"k": 4}
#     )

#     return retriever

from app.rag.pinecone_store import (
    get_vectorstore
)


def get_retriever():

    vectorstore = get_vectorstore()

    retriever = vectorstore.as_retriever(

        search_type="similarity",

        search_kwargs={
            "k": 6
        }
    )

    return retriever