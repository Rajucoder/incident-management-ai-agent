import re

from agent.state import AgentState
from agent.router import route_user_request


def extract_incident_id(user_input: str) -> int:
    match = re.search(r"\bincident\s*#?\s*(\d+)\b", user_input, re.IGNORECASE)
    if not match:
        raise ValueError("No incident ID found in the user input")

    return int(match.group(1))


def intent_node(state: AgentState):
    user_input = state["user_input"].lower()
    if "show" in user_input:
        state["intent"] = "get_incident"
        state["incident_id"] = extract_incident_id(user_input)

    elif "assign" in user_input:
        state["intent"] = "assign_incident"

    elif "priority" in user_input:
        state["intent"] = "update_priority"

    elif "resolve" in user_input:
        state["intent"] = "resolve_incident"

    return state

def execute_node(state: AgentState):
    intent = state["intent"]
    tool = route_user_request(intent)
    if intent == "get_incident":
        incident_id = state["incident_id"]
        result = tool(incident_id)
        state["result"] = result

    return state
