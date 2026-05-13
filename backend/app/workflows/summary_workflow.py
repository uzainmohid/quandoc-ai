from app.workflows.rag_workflow import (
    run_rag_workflow
)


def run_summary_workflow(question):

    context, docs = run_rag_workflow(
        question
    )

    summary_context = f"""
Provide a professional summary.

CONTEXT:
{context}
"""

    return summary_context, docs