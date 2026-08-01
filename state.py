from typing import TypedDict, List, Dict


class AgentState(TypedDict):

    question: str

    classification: str

    retrieved_docs: List[Dict]

    answer: str

    sources: List[Dict]

    confidence: float

    verified: bool

    retry_count: int

    reason: str

    requires_human: bool

    clarification_question: str

    warnings: List[str]