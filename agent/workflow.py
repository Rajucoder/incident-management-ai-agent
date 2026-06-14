from agent.state import AgentState
from agent.router import route_user_request

def intent_node(state: AgentState):
    user_input = state["user_input"].lower()
    if "show" in user_input:
        state["intent"] = "get_incident"
        state["incident_id"] = 1

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