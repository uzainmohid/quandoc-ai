def citation_agent(answer, docs):

    citations = []

    for doc in docs:

        source = doc.metadata.get(
            "source",
            "Unknown"
        )

        page = doc.metadata.get(
            "page",
            "Unknown"
        )

        citations.append(
            f"{source} - Page {page}"
        )

    return {
        "answer": answer,
        "citations": list(set(citations))
    }