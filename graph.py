from langgraph.graph import StateGraph, END

from state import AgentState
from config import MAX_RETRIES

from nodes.triage import triage_node
from nodes.retrieval import retrieval_node
from nodes.generator import generator_node
from nodes.verifier import verifier_node


# -----------------------------------------
# Route after Triage
# -----------------------------------------

def triage_router(state):
    """
    Route only answerable questions to retrieval.
    All other classifications end the workflow.
    """

    if state["classification"] == "answerable":
        return "retrieval"

    return END


# -----------------------------------------
# Route after Verification
# -----------------------------------------

def verification_router(state):
    """
    Decide whether to retry generation
    or finish the workflow.
    """

    # Verification successful
    if state.get("verified", False):
        return END

    # Stop if human intervention is required
    if state.get("requires_human", False):
        return END

    # Retry if retries remain
    if state.get("retry_count", 0) < MAX_RETRIES:
        return "generator"

    # Otherwise stop
    return END


# -----------------------------------------
# Build Graph
# -----------------------------------------

builder = StateGraph(AgentState)

# Nodes
builder.add_node("triage", triage_node)
builder.add_node("retrieval", retrieval_node)
builder.add_node("generator", generator_node)
builder.add_node("verifier", verifier_node)

# Entry Point
builder.set_entry_point("triage")

# -----------------------------------------
# Triage Routing
# -----------------------------------------

builder.add_conditional_edges(
    "triage",
    triage_router,
    {
        "retrieval": "retrieval",
        END: END,
    },
)

# -----------------------------------------
# Main Workflow
# -----------------------------------------

builder.add_edge("retrieval", "generator")
builder.add_edge("generator", "verifier")

# -----------------------------------------
# Verification Routing
# -----------------------------------------

builder.add_conditional_edges(
    "verifier",
    verification_router,
    {
        "generator": "generator",
        END: END,
    },
)

# -----------------------------------------
# Compile Graph
# -----------------------------------------

graph = builder.compile()