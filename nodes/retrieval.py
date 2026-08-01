from utils.embeddings import search
from config import TOP_K
from utils.logger import logger


def retrieval_node(state):
    """
    Retrieve relevant documents from the Knowledge Base
    and Resolved Cases.

    Priority:
    1. Knowledge Base
    2. Resolved Cases (excluding superseded)
    """

    question = state["question"]

    logger.info("Starting Retrieval Node...")

    results = search(
        query=question,
        top_k=TOP_K
    )

    knowledge_docs = []
    resolved_cases = []

    for doc in results:

        # Priority 1: Knowledge Base
        if doc["type"] == "knowledge_base":
            knowledge_docs.append(doc)

        # Priority 2: Resolved Cases
        elif doc["type"] == "resolved_case":

            if doc.get("status") != "superseded":
                resolved_cases.append(doc)

    final_results = knowledge_docs + resolved_cases

    state["retrieved_docs"] = final_results

    logger.info(f"Retrieved {len(final_results)} documents.")

    print("\n========== RETRIEVAL ==========")

    for doc in final_results:
        print(f"{doc['source_id']} ({doc['type']})")

    print("================================\n")

    return state