def route_question(question: str):

    question = question.lower()

    if "summarize" in question:
        return "summary"

    elif "compare" in question:
        return "comparison"

    return "rag"