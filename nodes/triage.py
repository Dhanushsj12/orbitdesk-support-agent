from utils.logger import logger


def triage_node(state):
    """
    Rule-based triage node.

    Classifications:
    - answerable
    - requires_clarification
    - requires_escalation
    - out_of_scope
    """

    logger.info("Starting Triage Node...")

    question = state["question"].lower().strip()

    # -----------------------------------------
    # Out of Scope
    # -----------------------------------------
    if any(word in question for word in [
        "refund",
        "billing",
        "cancel subscription",
        "payment"
    ]):

        state["classification"] = "out_of_scope"

        state["answer"] = (
            "This request is outside the scope of the OrbitDesk documentation. "
            "Please contact the appropriate billing or support team."
        )

        state["confidence"] = 1.0

        state["verified"] = True

        state["requires_human"] = False

        state["reason"] = "Out of scope."

        logger.info(f"Classification: {state['classification']}")

        return state

    # -----------------------------------------
    # Requires Clarification
    # -----------------------------------------
    elif len(question) < 15:

        state["classification"] = "requires_clarification"

        state["answer"] = (
            "Could you please provide more details so I can better assist you?"
        )

        state["confidence"] = 1.0

        state["verified"] = True

        state["requires_human"] = False

        state["reason"] = "More information required."

        logger.info(f"Classification: {state['classification']}")

        return state

    # -----------------------------------------
    # Requires Escalation
    # -----------------------------------------
    elif any(word in question for word in [
        "still fails",
        "already tried",
        "followed every",
        "doesn't work",
        "not working"
    ]):

        state["classification"] = "requires_escalation"

        state["answer"] = (
            "Based on your description, you have already completed the documented troubleshooting steps. "
            "This issue requires escalation to the OrbitDesk support team for further investigation."
        )

        state["confidence"] = 1.0

        state["verified"] = True

        state["requires_human"] = True

        state["reason"] = "Escalation required."

        logger.info(f"Classification: {state['classification']}")

        return state

    # -----------------------------------------
    # Answerable
    # -----------------------------------------
    else:

        state["classification"] = "answerable"

        logger.info(f"Classification: {state['classification']}")

        return state