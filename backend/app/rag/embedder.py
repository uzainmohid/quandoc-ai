# from langchain_community.embeddings import OllamaEmbeddings
# from langchain_community.vectorstores import Chroma

# CHROMA_DB_DIR = "chroma_db"

# embedding_model = OllamaEmbeddings(
#     model="nomic-embed-text"
# )


# def store_embeddings(chunks):

#     vector_db = Chroma.from_documents(
#         documents=chunks,
#         embedding=embedding_model,
#         persist_directory=CHROMA_DB_DIR
#     )

#     vector_db.persist()

#     return vector_db

# from langchain_community.embeddings import OllamaEmbeddings
# from langchain_community.vectorstores import Chroma

# CHROMA_DB_DIR = "chroma_db"

# embedding_model = OllamaEmbeddings(
#     model="nomic-embed-text"
# )


# def store_embeddings(chunks):

#     vector_db = Chroma.from_documents(
#         documents=chunks,
#         embedding=embedding_model,
#         persist_directory=CHROMA_DB_DIR,
#         collection_name="harvey_ai_docs"
#     )

#     return vector_db 

# from langchain_community.embeddings import OllamaEmbeddings
# from langchain_community.vectorstores import Chroma

# CHROMA_DB_DIR = "chroma_db"

# embedding_model = OllamaEmbeddings(
#     model="nomic-embed-text"
# )


# def store_embeddings(chunks, filename):

#     for chunk in chunks:

#         chunk.metadata["source"] = filename

#     vector_db = Chroma.from_documents(
#         documents=chunks,
#         embedding=embedding_model,
#         persist_directory=CHROMA_DB_DIR,
#         collection_name="harvey_ai_docs"
#     )

#     return vector_db 


# from langchain_community.embeddings import OllamaEmbeddings
# from langchain_community.vectorstores import Chroma

# CHROMA_DB_DIR = "chroma_db"

# embedding_model = OllamaEmbeddings(
#     model="nomic-embed-text"
# )


# def store_embeddings(chunks, filename):

#     for chunk in chunks:

#         chunk.metadata["source"] = filename

#     vector_db = Chroma(
#         persist_directory=CHROMA_DB_DIR,
#         embedding_function=embedding_model,
#         collection_name="harvey_ai_docs"
#     )

#     vector_db.add_documents(chunks)

#     return vector_db

from app.rag.pinecone_store import (
    get_vectorstore
)


def store_embeddings(
    chunks,
    filename
):

    vectorstore = get_vectorstore()

    texts = []

    metadatas = []

    for chunk in chunks:

        texts.append(
            chunk.page_content
        )

        metadatas.append({

            "source": filename,

            "page": chunk.metadata.get(
                "page",
                0
            )
        })

    vectorstore.add_texts(
        texts=texts,
        metadatas=metadatas
    )