# from app.agents.query_agent import process_query
# from app.agents.retrieval_agent import retrieve_documents
# from app.agents.reasoning_agent import reason_and_answer


# def run_workflow(question):

#     optimized_query = process_query(
#         question
#     )

#     docs = retrieve_documents(
#         optimized_query
#     )

#     context = "\n\n".join(
#         doc.page_content
#         for doc in docs
#     )

#     response = reason_and_answer(
#         context=context,
#         question=question
#     )

#     return response, docs

from app.workflows.orchestrator import (
    run_orchestrator
)

from app.rag.chat_engine import (
    generate_response
)


def run_workflow(question):

    context, docs = run_orchestrator(
        question
    )

    final_prompt = f"""
You are Harvey AI.

Answer professionally.

CONTEXT:
{context}

QUESTION:
{question}
"""

    response = generate_response(
        context=context,
        question=question
    )

    return response, docs