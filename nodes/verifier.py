from config import MAX_RETRIES
from utils.logger import logger


def verifier_node(state):
    """
    Rule-based verification.

    Ensures:
    - An answer exists
    - At least one supporting source exists
    - Confidence is reasonable
    """

    logger.info("Starting Verification Node...")

    # -----------------------------
    # No answer
    # -----------------------------
    if not state.get("answer", "").strip():

        logger.warning("Generated answer is empty.")

        state["verified"] = False
        state["reason"] = "Generated answer is empty."
        state["requires_human"] = True

        return state

    # -----------------------------
    # No sources
    # -----------------------------
    if len(state.get("sources", [])) == 0:

        logger.warning("No supporting sources.")

        state["verified"] = False
        state["reason"] = "No supporting sources."
        state["requires_human"] = True

        return state

    # -----------------------------
    # Confidence too low
    # -----------------------------
    if state.get("confidence", 0.0) < 0.3:

        logger.warning("Confidence too low.")

        retries = state.get("retry_count", 0)

        if retries < MAX_RETRIES:

            state["retry_count"] = retries + 1

            state["verified"] = False

            state["reason"] = "Retry generation."

            logger.info(
                f"Retry Count: {state['retry_count']}"
            )

            return state

        state["verified"] = False
        state["requires_human"] = True
        state["reason"] = "Low confidence after retries."

        return state

    # -----------------------------
    # Verification Passed
    # -----------------------------
    logger.info("Verification Passed.")

    state["verified"] = True
    state["reason"] = "Answer verified."

    return state