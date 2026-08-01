from models.llm import generate
from utils.logger import logger


GENERATION_PROMPT = """
You are an OrbitDesk support agent.

You are provided with internal OrbitDesk documentation.

Follow these rules exactly:

1. Answer ONLY from the supplied documentation.
2. Never use outside knowledge.
3. Never invent information.
4. Never say:
   - "I do not have access to the documentation."
   - "According to the provided evidence."
   - "As an AI..."
   - "Based on the context..."
5. If the answer cannot be found, reply exactly:
I cannot answer confidently using the available documentation.
6. Answer in 1-3 concise sentences.
7. Do NOT explain your reasoning.
8. Do NOT include "Sources:" in the answer.
9. Return ONLY the final answer.
"""


def generator_node(state):

    logger.info("Starting Generator Node...")

    question = state["question"]
    docs = state["retrieved_docs"]

    evidence = ""
    sources = []

    # Use top 2 retrieved documents
    for doc in docs[:2]:

        evidence += f"""
Source ID: {doc['source_id']}

{doc['content'][:700]}

"""

        sources.append({
            "source_id": doc["source_id"],
            "type": doc["type"]
        })

    prompt = f"""
{GENERATION_PROMPT}

Question:
{question}

Documentation:
{evidence}

Final Answer:
"""

    answer = generate(prompt).strip()

    # -------------------------
    # Cleanup
    # -------------------------

    unwanted = [
        "I do not have access to the OrbitDesk documentation.",
        "I do not have access to the documentation.",
        "According to the provided evidence,",
        "according to the provided evidence,",
        "Based on the provided evidence,",
        "based on the provided evidence,",
        "Based on the documentation,",
        "based on the documentation,",
        "However,",
        "Answer:",
        "Sources:"
    ]

    for phrase in unwanted:
        answer = answer.replace(phrase, "")

    answer = " ".join(answer.split())

    confidence = round(min(1.0, len(sources) * 0.45), 2)

    state["answer"] = answer
    state["sources"] = sources
    state["confidence"] = confidence

    logger.info("Answer Generated Successfully.")

    print("\n========== GENERATOR ==========")
    print(answer)
    print("================================\n")

    return state