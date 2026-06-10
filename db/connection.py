import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="incident_agent_db",
        user="postgres",
        password="",
    )

    return conn

