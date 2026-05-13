# import ollama

# SYSTEM_PROMPT = """
# You are Harvey AI.

# You are an advanced AI Document Intelligence Assistant.

# Answer ONLY using the provided document context.

# If the answer is not found in the document, say:
# 'I could not find this information in the uploaded documents.'

# Always provide clear and professional answers.
# """


# def generate_response(context, question):

#     prompt = f"""
# Context:
# {context}

# Question:
# {question}
# """

#     response = ollama.chat(
#         model="llama3.2",
#         messages=[
#             {
#                 "role": "system",
#                 "content": SYSTEM_PROMPT
#             },
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     )

#     return response["message"]["content"] 

# import ollama

# SYSTEM_PROMPT = """
# You are Harvey AI.

# You are an elite enterprise-grade AI Document Intelligence Assistant.

# Your responsibilities:
# - Answer ONLY using retrieved document context
# - Provide highly accurate grounded answers
# - Never hallucinate
# - Mention uncertainty when context is insufficient
# - Summarize professionally
# - Extract key business insights
# - Explain technical concepts clearly

# Response style:
# - Professional
# - Structured
# - Concise but informative

# If answer is not found:
# 'I could not find this information in the uploaded documents.'
# """


# def generate_response(context, question):

#     prompt = f"""
# DOCUMENT CONTEXT:
# {context}

# USER QUESTION:
# {question}

# Generate a grounded answer from the document only.
# """

#     response = ollama.chat(
#         model="llama3.2",
#         messages=[
#             {
#                 "role": "system",
#                 "content": SYSTEM_PROMPT
#             },
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     )

#     return response["message"]["content"]




import ollama

from app.rag.memory import (
    add_to_memory,
    get_memory_context
)

from app.rag.prompt_engine import build_prompt


def generate_response(context, question):

    memory_context = get_memory_context()

    final_prompt = build_prompt(
        context=context,
        memory=memory_context,
        question=question
    )

    stream = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ],
        stream=True
    )

    full_response = ""

    for chunk in stream:

        content = chunk["message"]["content"]

        full_response += content

    add_to_memory(
        question,
        full_response
    )

    return full_response
    