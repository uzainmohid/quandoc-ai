import ollama


def rewrite_query(question):

    prompt = f"""
Rewrite this user question into a highly clear semantic search query.

User Question:
{question}

Optimized Search Query:
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]