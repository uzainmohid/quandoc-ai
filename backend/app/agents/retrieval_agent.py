# from app.rag.retriever import get_retriever
# from app.rag.reranker import rerank_documents


# def retrieve_documents(question):

#     retriever = get_retriever()

#     docs = retriever.invoke(question)

#     reranked_docs = rerank_documents(
#         question,
#         docs
#     )

#     return reranked_docs

def retrieval_agent(question):

    return f"""
You are a retrieval optimization agent.

Improve retrieval quality for:

QUESTION:
{question}

Generate:
- semantic query
- keyword query
- analytical query
"""