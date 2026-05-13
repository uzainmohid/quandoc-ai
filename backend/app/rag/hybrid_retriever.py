# from rank_bm25 import BM25Okapi

# documents_store = []


# def setup_bm25(chunks):

#     global documents_store

#     documents_store = chunks

#     tokenized_docs = [
#         doc.page_content.split()
#         for doc in chunks
#     ]

#     bm25 = BM25Okapi(tokenized_docs)

#     return bm25


# def bm25_search(bm25, query, top_k=3):

#     tokenized_query = query.split()

#     results = bm25.get_top_n(
#         tokenized_query,
#         documents_store,
#         n=top_k
#     )

#     return results 

# from typing import List
# from collections import defaultdict
# from langchain_core.documents import Document

# from rank_bm25 import BM25Okapi

# from app.rag.pinecone_store import vectorstore


# class AdvancedHybridRetriever:

#     def __init__(self):

#         self.vectorstore = vectorstore

#     # =========================
#     # BM25 RETRIEVAL
#     # =========================

#     def bm25_search(
#         self,
#         query: str,
#         documents: List[Document],
#         top_k: int = 5
#     ):

#         tokenized_docs = [
#             doc.page_content.lower().split()
#             for doc in documents
#         ]

#         bm25 = BM25Okapi(tokenized_docs)

#         tokenized_query = query.lower().split()

#         scores = bm25.get_scores(tokenized_query)

#         ranked = sorted(
#             zip(documents, scores),
#             key=lambda x: x[1],
#             reverse=True
#         )

#         return ranked[:top_k]

#     # =========================
#     # VECTOR SEARCH
#     # =========================

#     def semantic_search(
#         self,
#         query: str,
#         top_k: int = 10
#     ):

#         docs = self.vectorstore.similarity_search_with_score(
#             query,
#             k=top_k
#         )

#         return docs

#     # =========================
#     # HYBRID FUSION
#     # =========================

#     def hybrid_search(
#         self,
#         query: str,
#         top_k: int = 5
#     ):

#         semantic_results = self.semantic_search(
#             query=query,
#             top_k=10
#         )

#         semantic_docs = [
#             doc for doc, _ in semantic_results
#         ]

#         bm25_results = self.bm25_search(
#             query=query,
#             documents=semantic_docs,
#             top_k=10
#         )

#         score_map = defaultdict(float)

#         # semantic score fusion
#         for rank, (doc, score) in enumerate(semantic_results):

#             content = doc.page_content

#             semantic_weight = 1 / (rank + 1)

#             score_map[content] += semantic_weight * 0.7

#         # bm25 score fusion
#         for rank, (doc, score) in enumerate(bm25_results):

#             content = doc.page_content

#             bm25_weight = 1 / (rank + 1)

#             score_map[content] += bm25_weight * 0.3

#         final_docs = []

#         used = set()

#         sorted_results = sorted(
#             score_map.items(),
#             key=lambda x: x[1],
#             reverse=True
#         )

#         for content, score in sorted_results:

#             if content in used:
#                 continue

#             used.add(content)

#             matched_doc = next(
#                 (
#                     d for d, _ in semantic_results
#                     if d.page_content == content
#                 ),
#                 None
#             )

#             if matched_doc:
#                 final_docs.append(matched_doc)

#             if len(final_docs) >= top_k:
#                 break

#         return final_docs


# hybrid_retriever = AdvancedHybridRetriever()


from typing import List
from collections import defaultdict

from langchain_core.documents import Document

from rank_bm25 import BM25Okapi

from app.rag.pinecone_store import get_vectorstore


# =========================
# INITIALIZE VECTORSTORE
# =========================

vectorstore = get_vectorstore()


class AdvancedHybridRetriever:

    def __init__(self):

        self.vectorstore = vectorstore

    # =========================
    # BM25 RETRIEVAL
    # =========================

    def bm25_search(
        self,
        query: str,
        documents: List[Document],
        top_k: int = 5
    ):

        tokenized_docs = [
            doc.page_content.lower().split()
            for doc in documents
        ]

        bm25 = BM25Okapi(tokenized_docs)

        tokenized_query = query.lower().split()

        scores = bm25.get_scores(tokenized_query)

        ranked = sorted(
            zip(documents, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked[:top_k]

    # =========================
    # VECTOR SEARCH
    # =========================

    def semantic_search(
        self,
        query: str,
        top_k: int = 10
    ):

        docs = self.vectorstore.similarity_search_with_score(
            query,
            k=top_k
        )

        return docs

    # =========================
    # HYBRID FUSION
    # =========================

    def hybrid_search(
        self,
        query: str,
        top_k: int = 5
    ):

        semantic_results = self.semantic_search(
            query=query,
            top_k=10
        )

        semantic_docs = [
            doc for doc, _ in semantic_results
        ]

        bm25_results = self.bm25_search(
            query=query,
            documents=semantic_docs,
            top_k=10
        )

        score_map = defaultdict(float)

        # semantic score fusion
        for rank, (doc, score) in enumerate(semantic_results):

            content = doc.page_content

            semantic_weight = 1 / (rank + 1)

            score_map[content] += semantic_weight * 0.7

        # bm25 score fusion
        for rank, (doc, score) in enumerate(bm25_results):

            content = doc.page_content

            bm25_weight = 1 / (rank + 1)

            score_map[content] += bm25_weight * 0.3

        final_docs = []

        used = set()

        sorted_results = sorted(
            score_map.items(),
            key=lambda x: x[1],
            reverse=True
        )

        for content, score in sorted_results:

            if content in used:
                continue

            used.add(content)

            matched_doc = next(
                (
                    d for d, _ in semantic_results
                    if d.page_content == content
                ),
                None
            )

            if matched_doc:
                final_docs.append(matched_doc)

            if len(final_docs) >= top_k:
                break

        return final_docs


hybrid_retriever = AdvancedHybridRetriever()