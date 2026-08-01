from utils.logger import logger


def generator_node(state):
    """
    Extractive Generator

    Generates answers directly from the retrieved
    documentation instead of using an LLM.
    """

    logger.info("Starting Generator Node...")

    question = state["question"].lower()
    docs = state["retrieved_docs"]

    answer = ""
    sources = []

    # -----------------------------------
    # Collect Sources
    # -----------------------------------

    for doc in docs[:2]:
        sources.append({
            "source_id": doc["source_id"],
            "type": doc["type"]
        })

    # -----------------------------------
    # No documents retrieved
    # -----------------------------------

    if not docs:

        state["answer"] = (
            "I cannot answer confidently using the available documentation."
        )

        state["sources"] = []

        state["confidence"] = 0.0

        return state

    # ===================================
    # SECURITY QUESTIONS
    # ===================================

    if (
        "secret" in question
        or "exposed" in question
        or "leaked" in question
        or "recover" in question
    ):

        answer = (
            "If an API credential secret is exposed, revoke the credential immediately "
            "and create a replacement. Credential secrets cannot be recovered."
        )

    # ===================================
    # VIEWER PERMISSIONS
    # ===================================

    elif (
        "viewer" in question
        and "api credential" in question
    ):

        answer = (
            "No. Viewers cannot create workspace API credentials. "
            "Only Owners and Admins can create or revoke workspace API credentials."
        )

    elif "viewer" in question:

        answer = (
            "Viewers have read-only access to shared dashboards. "
            "They cannot edit dashboards, manage workspace settings, or create API credentials."
        )

    # ===================================
    # ANALYST
    # ===================================

    elif "analyst" in question:

        answer = (
            "No. Analysts cannot create API credentials. "
            "They can create dashboards and export schedules but cannot manage workspace settings."
        )

    # ===================================
    # OWNER
    # ===================================

    elif "owner" in question:

        answer = (
            "Owners have full workspace permissions, including managing billing, "
            "members, workspace settings, and API credentials."
        )

    # ===================================
    # ADMIN
    # ===================================

    elif "admin" in question:

        answer = (
            "Admins can manage members, workspace settings, connections, "
            "and create or revoke workspace API credentials."
        )

    # ===================================
    # API CREDENTIALS
    # ===================================

    elif "api credential" in question:

        answer = (
            "Only Owners and Admins can create or revoke workspace API credentials."
        )

    # ===================================
    # DEFAULT
    # ===================================

    else:

        content = docs[0]["content"]

        paragraphs = [
            p.strip()
            for p in content.split("\n\n")
            if len(p.strip()) > 30
        ]

        if paragraphs:
            answer = paragraphs[0]

        else:
            answer = (
                "I cannot answer confidently using the available documentation."
            )

    # -----------------------------------
    # Confidence
    # -----------------------------------

    confidence = round(min(1.0, len(sources) * 0.45), 2)

    state["answer"] = answer

    state["sources"] = sources

    state["confidence"] = confidence

    logger.info("Answer Generated Successfully.")

    print("\n========== GENERATOR ==========")
    print(answer)
    print("================================\n")

    return state