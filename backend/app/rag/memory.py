# conversation_memory = []


# def add_to_memory(question, answer):

#     conversation_memory.append({
#         "question": question,
#         "answer": answer
#     })

#     # keep only recent history
#     if len(conversation_memory) > 5:
#         conversation_memory.pop(0)


# def get_memory_context():

#     memory_text = ""

#     for item in conversation_memory:

#         memory_text += f"""
# User: {item['question']}
# Assistant: {item['answer']}
# """

#     return memory_text 


import json
import os

MEMORY_FILE = "memory.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):

        return []

    with open(MEMORY_FILE, "r") as f:

        return json.load(f)


def save_memory(memory):

    with open(MEMORY_FILE, "w") as f:

        json.dump(memory, f)


def add_to_memory(question, answer):

    memory = load_memory()

    memory.append({
        "question": question,
        "answer": answer
    })

    memory = memory[-5:]

    save_memory(memory)


def get_memory_context():

    memory = load_memory()

    text = ""

    for item in memory:

        text += f"""
User: {item['question']}
Assistant: {item['answer']}
"""

    return text