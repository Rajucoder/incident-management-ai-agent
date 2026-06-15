from typing import TypedDict, NotRequired

class AgentState(TypedDict):
    user_input: str
    intent: NotRequired[str]
    incident_id: NotRequired[int]
    assigned_to: NotRequired[str]
    priority: NotRequired[str]
    resolution: NotRequired[str]
    result: NotRequired[object]