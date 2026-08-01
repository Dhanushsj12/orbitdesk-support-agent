from models.llm import generate
from utils.logger import logger


GENERATION_PROMPT = """
You are OrbitDesk Support Assistant.

You MUST follow these rules:

1. Answer ONLY using the supplied evidence.
2. Never use outside knowledge.
3. Never hallucinate.
4. If the evidence is insufficient, say:
   "I cannot answer confidently using the available documentation."
5. Mention the source IDs used.
6. Keep the answer clear and concise.
"""


def generator_node(state):
    """
    Generate an answer using the retrieved documents.
    """

    logger.info("Starting Generator Node...")

    question = state["question"]

    docs = state["retrieved_docs"]

    evidence = ""

    sources = []

    for doc in docs:

        evidence += f"""

=========================
Source ID:
{doc['source_id']}

Content:
{doc['content']}
=========================

"""

        sources.append({
            "source_id": doc["source_id"],
            "type": doc["type"]
        })

    prompt = f"""
{GENERATION_PROMPT}

Question:

{question}

Evidence:

{evidence}

Final Answer:
"""

    answer = generate(prompt)

    # Simple confidence calculation
    confidence = min(
        1.0,
        len(docs) * 0.30
    )

    state["answer"] = answer.strip()

    state["sources"] = sources

    state["confidence"] = round(confidence, 2)

    logger.info("Answer Generated Successfully.")

    print("\n========== GENERATOR ==========")
    print(state["answer"])
    print("================================\n")

    return state