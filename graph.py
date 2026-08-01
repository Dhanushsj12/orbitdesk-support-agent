from langgraph.graph import StateGraph, END

from state import AgentState

from nodes.triage import triage_node
from nodes.retrieval import retrieval_node
from nodes.generator import generator_node
from nodes.verifier import verifier_node


# -----------------------------------------
# Routing after Triage
# -----------------------------------------

def triage_router(state):

    classification = state["classification"]

    if classification == "answerable":
        return "retrieval"

    return END


# -----------------------------------------
# Routing after Verification
# -----------------------------------------

def verification_router(state):

    if state["verified"]:
        return END

    if state.get("retry_count", 0) > 0:
        return "generator"

    return END


# -----------------------------------------
# Build Graph
# -----------------------------------------

builder = StateGraph(AgentState)

builder.add_node("triage", triage_node)

builder.add_node("retrieval", retrieval_node)

builder.add_node("generator", generator_node)

builder.add_node("verifier", verifier_node)


builder.set_entry_point("triage")


builder.add_conditional_edges(
    "triage",
    triage_router,
    {
        "retrieval": "retrieval",
        END: END,
    },
)


builder.add_edge(
    "retrieval",
    "generator"
)

builder.add_edge(
    "generator",
    "verifier"
)


builder.add_conditional_edges(
    "verifier",
    verification_router,
    {
        "generator": "generator",
        END: END,
    },
)


graph = builder.compile()