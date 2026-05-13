from app.rag.chat_engine import generate_response


def reason_and_answer(context, question):

    response = generate_response(
        context=context,
        question=question
    )

    return response