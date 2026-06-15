import re

from agent.state import AgentState
from agent.router import route_user_request


def extract_incident_id(user_input: str) -> int:
    match = re.search(r"\bincident\s*#?\s*(\d+)\b", user_input, re.IGNORECASE)
    if not match:
        raise ValueError("No incident ID found in the user input")

    return int(match.group(1))

def extract_assignment(user_input: str) -> tuple[int, str]:
    match = re.search(
        r"\bassign\s+incident\s*#?\s*(\d+)\s+to\s+(.+?)\s*$",
        user_input,
        re.IGNORECASE,
    )
    if not match:
        raise ValueError("No incident ID or assignee found")

    return int(match.group(1)), match.group(2).strip()


def extract_priority_update(user_input: str) -> tuple[int, str]:
    match = re.search(
        r"\bupdate\s+priority\s+of\s+incident\s*#?\s*(\d+)\s+to\s+(\w+)\s*$",
        user_input,
        re.IGNORECASE,
    )
    if not match:
        raise ValueError("No incident ID or priority found")

    return int(match.group(1)), match.group(2).strip()


def extract_resolution(user_input: str) -> tuple[int, str]:
    match = re.search(
        r"\bresolve\s+incident\s*#?\s*(\d+)\s+with\s+resolution\s+(.+?)\s*$",
        user_input,
        re.IGNORECASE,
    )
    if not match:
        raise ValueError("No incident ID or resolution found")

    return int(match.group(1)), match.group(2).strip()

def intent_node(state: AgentState):
    user_input = state["user_input"]
    normalized_input = user_input.lower()

    if "show" in normalized_input:
        state["intent"] = "get_incident"
        state["incident_id"] = extract_incident_id(user_input)

    elif "assign" in normalized_input:
        state["intent"] = "assign_incident"
        state["incident_id"], state["assigned_to"] = extract_assignment(user_input)

    elif "priority" in normalized_input:
        state["intent"] = "update_priority"
        state["incident_id"], state["priority"] = extract_priority_update(user_input)

    elif "resolve" in normalized_input:
        state["intent"] = "resolve_incident"
        state["incident_id"], state["resolution"] = extract_resolution(user_input)

    return state

def execute_node(state: AgentState):
    intent = state["intent"]
    tool = route_user_request(intent)
    if intent == "get_incident":
        incident_id = state["incident_id"]
        result = tool(incident_id)
        state["result"] = result
    elif intent == "assign_incident":
        incident_id = state["incident_id"]
        assigned_to = state["assigned_to"]
        result = tool(incident_id, assigned_to)
        state["result"] = result
    elif intent == "update_priority":
        incident_id = state["incident_id"]
        priority = state["priority"]
        result = tool(incident_id, priority)
        state["result"] = result
    elif intent == "resolve_incident":
        incident_id = state["incident_id"]
        resolution = state["resolution"]
        result = tool(incident_id, resolution)
        state["result"] = result

    return state
