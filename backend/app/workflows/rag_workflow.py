# # from app.rag.retriever import get_retriever
# # from app.rag.query_rewriter import rewrite_query
# # from app.rag.reranker import rerank_documents 
# # from app.rag.hybrid_retriever import hybrid_retriever
# # from app.rag.reranker import reranker


# # def run_rag_workflow(question):

# #     retriever = get_retriever()

# #     optimized_query = rewrite_query(
# #         question
# #     )

# #     docs = retriever.invoke(
# #         optimized_query
# #     )

# #     reranked_docs = rerank_documents(
# #         optimized_query,
# #         docs
# #     )

# #     context = "\n\n".join(
# #         doc.page_content
# #         for doc in reranked_docs
# #     )

# #     return context, reranked_docs

# from app.rag.query_rewriter import rewrite_query

# from app.rag.hybrid_retriever import hybrid_retriever

# from app.rag.reranker import reranker


# def run_rag_workflow(question):

#     # =========================
#     # QUERY OPTIMIZATION
#     # =========================

#     optimized_query = rewrite_query(
#         question
#     )

#     # =========================
#     # HYBRID RETRIEVAL
#     # =========================

#     docs = hybrid_retriever.hybrid_search(
#         optimized_query
#     )

#     # =========================
#     # ADVANCED RERANKING
#     # =========================

#     reranked_docs = reranker.rerank(
#         optimized_query,
#         docs
#     )

#     # =========================
#     # CONTEXT BUILDING
#     # =========================

#     context = "\n\n".join(
#         doc.page_content
#         for doc in reranked_docs
#     )

#     return context, reranked_docs

from app.rag.retriever import get_retriever
from app.rag.query_rewriter import rewrite_query

from app.rag.hybrid_retriever import hybrid_retriever
from app.rag.reranker import reranker


def run_rag_workflow(question):

    retriever = get_retriever()

    optimized_query = rewrite_query(
        question
    )

    # VECTOR SEARCH
    vector_docs = retriever.invoke(
        optimized_query
    )

    # HYBRID SEARCH
    hybrid_docs = hybrid_retriever.hybrid_search(
        optimized_query
    )

    # COMBINE RESULTS
    docs = vector_docs + hybrid_docs

    # REMOVE DUPLICATES
    unique_docs = []

    seen = set()

    for doc in docs:

        content = doc.page_content[:200]

        if content not in seen:

            seen.add(content)

            unique_docs.append(doc)

    # RERANK
    reranked_docs = reranker.rerank(
        optimized_query,
        unique_docs
    )

    # FINAL CONTEXT
    context = "\n\n".join(
        doc.page_content
        for doc in reranked_docs[:5]
    )

    return context, reranked_docs[:5]