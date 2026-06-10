from db.incident_repository import  (get_all_incidents,
                                     get_incident_by_id,
                                     update_priority)

print(get_all_incidents())

print(get_incident_by_id(1))

update_priority(1, "Critical")

print(get_incident_by_id(1))
