#KPI Database
import sqlite3

def get_connection(database_file):
    return sqlite3.connect(database_file)

def get_total_records(database_file):
    conn = get_connection(database_file)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM machine_data")
    result = cursor.fetchone()[0]

    conn.close()
    return result

def get_total_alarms(database_file):
    conn = get_connection(database_file)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM machine_data
        WHERE result != 'OK'
        """
        )
    
    result = cursor.fetchone()[0]
    conn.close()

    return result

def get_critical_alarms(database_file):
    conn = get_connection(database_file)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM machine_data
        WHERE result LIKE '%Critical%'
        """
        )
    
    result = cursor.fetchone()[0]
    conn.close()

    return result

def get_alarm_summary(database_file):
    conn = get_connection(database_file)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT result, COUNT(*)
        FROM machine_data
        WHERE result != 'OK'
        GROUP BY result
        ORDER BY COUNT(*) DESC
        """
    )

    result = cursor.fetchall()

    conn.close()
    return result


