def route_user_request(intent):
    if intent == "get_incident":
        return "get_incident_tool"

    elif intent == "assign_incident":
        return "assign_incident_tool"

    elif intent == "update_priority":
        return "update_priority_tool"

    elif intent == "resolve_incident":
        return "resolve_incident_tool"