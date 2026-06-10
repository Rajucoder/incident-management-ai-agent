from db.incident_repository import (
    get_incident_by_id,
    update_priority,
    assign_incident,
    resolve_incident
)


def get_incident_tool(incident_id):
    return get_incident_by_id(incident_id)


def update_priority_tool(incident_id, priority):
    update_priority(incident_id, priority)
    return f"Priority updated to {priority}"


def assign_incident_tool(incident_id, assigned_to):
    assign_incident(incident_id, assigned_to)
    return f"Incident assigned to {assigned_to}"


def resolve_incident_tool(incident_id, resolution):
    resolve_incident(incident_id, resolution)
    return "Incident resolved"