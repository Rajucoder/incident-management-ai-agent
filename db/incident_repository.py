from db.connection import get_connection

def get_all_incidents():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM incidents")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return rows

def get_incident_by_id(incident_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM incidents WHERE incident_id = %s", (incident_id,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return rows

def update_priority(incident_id, priority):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE incidents SET priority = %s WHERE incident_id = %s", (priority, incident_id))
    conn.commit()
    cursor.close()
    conn.close()

#create_incident()
def create_incident(title, status, priority, assigned_to):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO incidents
        (title, status, priority, assigned_to)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (title, status, priority, assigned_to)
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("Incident created successfully")
#assign_incident()
def assign_incident(incident_id, assigned_to):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE incidents
        SET assigned_to = %s
        WHERE incident_id = %s
    """

    cursor.execute(
        query,
        (assigned_to, incident_id)
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("Incident assigned successfully")

#resolve_incident()
def resolve_incident(incident_id, resolution):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE incidents
        SET status = %s,
            resolution = %s
        WHERE incident_id = %s
    """

    cursor.execute(
        query,
        (
            "Resolved",
            resolution,
            incident_id
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("Incident resolved successfully")

#create_audit_log()
def create_audit_log(
        action,
        old_value,
        new_value,
        performed_by):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO audit_logs
        (
            action,
            old_value,
            new_value,
            performed_by
        )
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            action,
            old_value,
            new_value,
            performed_by
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("Audit log created")