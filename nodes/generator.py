from models.llm import generate


GENERATION_PROMPT = """
You are OrbitDesk Support Assistant.

Rules:

1. Answer ONLY from the supplied evidence.

2. If evidence is insufficient,
say you cannot answer confidently.

3. Never invent steps.

4. Never use outside knowledge.

5. Always mention the supporting source IDs.

6. Return only the answer.
"""


def generator_node(state):

    question = state["question"]

    docs = state["retrieved_docs"]

    evidence = ""

    sources = []

    for doc in docs:

        evidence += f"""

Source:
{doc['source_id']}

Content:
{doc['content']}

"""

        sources.append(
            {
                "source_id": doc["source_id"],
                "passage": "Retrieved Context"
            }
        )

    prompt = f"""
{GENERATION_PROMPT}

Question:

{question}

Evidence:

{evidence}

Answer:
"""

    answer = generate(prompt)

    state["answer"] = answer

    state["sources"] = sources

    state["confidence"] = 0.90

    print("\n========== GENERATOR ==========")
    print(answer)
    print("================================\n")

    return state