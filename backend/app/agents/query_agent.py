from app.rag.query_rewriter import rewrite_query


def process_query(question):

    rewritten_query = rewrite_query(
        question
    )

    return rewritten_query