from db.incident_repository import  (get_all_incidents,
                                     get_incident_by_id,
                                     update_priority,
                                     create_incident,
                                     assign_incident,
                                     resolve_incident,
                                     create_audit_log)

print(get_all_incidents())

print(get_incident_by_id(1))

update_priority(1, "Critical")

print(get_incident_by_id(1))

create_incident(
    title="CPU Usage High",
    status="Open",
    priority="Medium",
    assigned_to="Raji"
)

assign_incident(
    incident_id=1,
    assigned_to="John"
)

resolve_incident(
    incident_id=1,
    resolution="Restarted database service"
)

create_audit_log(
    action="Priority Update",
    old_value="High",
    new_value="Critical",
    performed_by="Raji"
)
