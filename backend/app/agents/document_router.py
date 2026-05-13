def detect_document_intent(question, docs):

    question_lower = question.lower()

    matched_docs = []

    for doc in docs:

        source = doc.metadata.get(
            "source",
            ""
        ).lower()

        if source in question_lower:

            matched_docs.append(doc)

    if matched_docs:

        return matched_docs

    return docs