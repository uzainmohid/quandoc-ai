from app.workflows.rag_workflow import (
    run_rag_workflow
)


def run_compare_workflow(question):

    context, docs = run_rag_workflow(
        question
    )

    comparison_context = f"""
Compare the concepts professionally.

CONTEXT:
{context}
"""

    return comparison_context, docs