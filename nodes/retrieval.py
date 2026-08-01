from utils.embeddings import search
from config import TOP_K


def retrieval_node(state):
    """
    Retrieve relevant documents from the knowledge base
    and resolved cases.
    """

    question = state["question"]

    results = search(
        query=question,
        top_k=TOP_K
    )

    filtered_results = []

    for doc in results:

        # Skip superseded resolved cases
        if (
            doc.get("type") == "resolved_case"
            and doc.get("status") == "superseded"
        ):
            continue

        filtered_results.append(doc)

    state["retrieved_docs"] = filtered_results

    print("\n========== RETRIEVAL ==========")

    for doc in filtered_results:
        print(
            f"{doc['source_id']}  ({doc['type']})"
        )

    print("===============================\n")

    return state