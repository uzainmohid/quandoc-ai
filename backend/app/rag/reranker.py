# from sentence_transformers import CrossEncoder

# reranker_model = CrossEncoder(
#     "cross-encoder/ms-marco-MiniLM-L-6-v2"
# )


# def rerank_documents(question, docs):

#     pairs = [
#         [question, doc.page_content]
#         for doc in docs
#     ]

#     scores = reranker_model.predict(pairs)

#     ranked = sorted(
#         zip(scores, docs),
#         key=lambda x: x[0],
#         reverse=True
#     )

#     reranked_docs = [
#         doc
#         for score, doc in ranked
#     ]

#     return reranked_docs[:3]

from typing import List

from langchain_core.documents import Document


class SimpleReranker:

    def rerank(
        self,
        query: str,
        docs: List[Document]
    ):

        query_words = set(
            query.lower().split()
        )

        scored_docs = []

        for doc in docs:

            content_words = set(
                doc.page_content.lower().split()
            )

            overlap = len(
                query_words.intersection(content_words)
            )

            semantic_bonus = min(
                len(doc.page_content) / 1000,
                1
            )

            final_score = overlap + semantic_bonus

            scored_docs.append(
                (doc, final_score)
            )

        ranked = sorted(
            scored_docs,
            key=lambda x: x[1],
            reverse=True
        )

        return [
            doc for doc, score in ranked
        ]


reranker = SimpleReranker()