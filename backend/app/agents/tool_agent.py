def detect_tool(question):

    q = question.lower()

    if "compare" in q:
        return "comparison"

    elif "summarize" in q:
        return "summary"

    elif "risk" in q:
        return "risk_analysis"

    elif "architecture" in q:
        return "technical_analysis"

    return "general_qa"