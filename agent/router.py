from agent.incident_tools import (get_incident_tool,
                                  assign_incident_tool,
                                  update_priority_tool,
                                  resolve_incident_tool)

def route_user_request(intent):
    routes = {
        "get_incident_tool": get_incident_tool,
        "assign_incident": assign_incident_tool,
        "update_priority": update_priority_tool,
        "resolve_incident": resolve_incident_tool
    }
    return routes.get(intent)