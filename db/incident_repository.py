from db.connection import get_connection

def get_all_incidents():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM incidents")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return rows

def get_incident_by_id(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM incidents WHERE incident_id = %s", (id,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return rows

def update_priority(id, priority):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE incidents SET priority = %s WHERE incident_id = %s", (priority, id))
    conn.commit()
    cursor.close()
    conn.close()

#create_incident()

#assign_incident()

#resolve_incident()

#create_audit_log()