from app.agents.semantic_router import (
    route_question
)

from app.workflows.rag_workflow import (
    run_rag_workflow
)

from app.workflows.summary_workflow import (
    run_summary_workflow
)

from app.workflows.compare_workflow import (
    run_compare_workflow
)


def run_orchestrator(question):

    workflow = route_question(
        question
    )

    if workflow == "summary":

        return run_summary_workflow(
            question
        )

    elif workflow == "comparison":

        return run_compare_workflow(
            question
        )

    return run_rag_workflow(
        question
    )