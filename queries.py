# Query functions for database operations

import sqlite3

def show_all_records():

    conn = sqlite3.connect('factory.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM machines")
    print ("All Machine Records:")
    records = cursor.fetchall()
    for record in records:
        print(record)
    conn.close()

def show_alarms_only():

    conn = sqlite3.connect('factory.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM machines
    WHERE result != 'OK'
    """)
    print ("Show Alarms Only:")
    records = cursor.fetchall()
    for record in records:
        print(record)
    conn.close()

def show_stopped_machines():
    conn = sqlite3.connect('factory.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM machines
    WHERE status = 'STOPPED'
    """)
    print("Show Stopped Machines:")
    records = cursor.fetchall()
    for record in records:
        print(record)
    conn.close()

def show_critical_alarms():
    conn = sqlite3.connect('factory.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM machines
    WHERE result = 'Critical Temperature Alarm'
    """)
    print("Show Critical Alarms:")
    records = cursor.fetchall()
    for record in records:
        print(record)
    conn.close()

def show_running_machines():
    conn = sqlite3.connect('factory.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM machines
    WHERE status = 'RUNNING'
    """)
    print("Show Running Machines:")
    records = cursor.fetchall()
    for record in records:
        print(record)
    conn.close()

def show_machines_type(machine_type):
    conn = sqlite3.connect('factory.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM machines
    WHERE machine_type = ?
    """, (machine_type,))

    print(f"Show Machines of Type: {machine_type}")
    records = cursor.fetchall()
    for record in records:
        print(record)
    conn.close()

def count_machines_type():
    conn = sqlite3.connect('factory.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT machine_type, COUNT(*)
    FROM machines
    GROUP BY machine_type
    """)
    print ("Count of Machines by type:")
    records = cursor.fetchall()
    for record in records:
        print(record)
    
    conn.close()

def count_result():
    conn = sqlite3.connect('factory.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT result, COUNT(*)
    FROM machines
    GROUP BY result
    ORDER BY COUNT(*) DESC
    """)
    print ("Count of Machines by result:")
    records = cursor.fetchall()
    for record in records:
        print(record)
        
    conn.close()

def count_events():
    conn = sqlite3.connect('factory.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT machine_id, COUNT(*)
    FROM machines
    GROUP BY machine_id
    ORDER BY COUNT(*) DESC
    """)
    print ("Count of Events by Machine ID:")
    records = cursor.fetchall()
    for record in records:
        print(record)
    
    conn.close()
    
def count_critical_alarms():
    conn = sqlite3.connect('factory.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM machines
    WHERE result LIKE '%Critical%'
    """)
    print ("Count of Critical Alarms:")
    count = cursor.fetchone()[0]
    print(count)
    
    conn.close()

def get_alarm_summary():
    conn = sqlite3.connect('factory.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM machines
    WHERE status = 'STOPPED'
    """)
    print ("Alarm Summary:")
    count = cursor.fetchone()[0]
    print(f"Machine Stopped: {count}")

    cursor.execute("""
    SELECT COUNT(*)
    FROM machines
    WHERE result LIKE '%Temperature%'
    """)
    count = cursor.fetchone()[0]
    print(f"Temperature Alarm: {count}")

    cursor.execute("""
    SELECT COUNT(*)
    FROM machines
    WHERE result LIKE '%Pressure%'
    """)
    count = cursor.fetchone()[0]
    print(f"Pressure Alarm: {count}")

    cursor.execute("""
    SELECT COUNT(*)
    FROM machines
    WHERE result LIKE '%Critical%'
    """)
    count = cursor.fetchone()[0]
    print(f"Critical Temperature Alarm: {count}")

    conn.close()

def get_machine_event_counts():
    conn = sqlite3.connect('factory.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT machine_id, COUNT(*)
    FROM machines
    WHERE result != 'OK'
    GROUP BY machine_id
    ORDER BY COUNT(*) DESC
    """)
    print ("Machine Event Counts:")
    records = cursor.fetchall()
    for record in records:
        print(record)
    
    conn.close()

def factory_kpi_report():
    conn = sqlite3.connect('factory.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT 
        (SELECT COUNT(*) FROM machines) AS total_machines,
        (SELECT COUNT(*) FROM machines WHERE status = 'RUNNING') AS running_machines,
        (SELECT COUNT(*) FROM machines WHERE status = 'STOPPED') AS stopped_machines,
        (SELECT COUNT(*) FROM machines WHERE result != 'OK') AS total_alarms,
        (SELECT COUNT(*) FROM machines WHERE result LIKE '%Critical%') AS critical_alarms
    """)
    print("================================")
    print ("FACTORY KPI REPORT:")
    print("================================")
    report = cursor.fetchone()
    print(f"Total Machines: {report[0]}")
    print(f"Running Machines: {report[1]}")
    print(f"Stopped Machines: {report[2]}")
    print(f"Total Alarms: {report[3]}")
    print(f"Critical Alarms: {report[4]}")

    cursor.execute("""
    SELECT result, COUNT(*)
    FROM machines
    WHERE result != 'Ok'
    GROUP BY result
    ORDER BY COUNT(*) DESC
    LIMIT 1
    """)
    print ("Most Common Alarm:")
    record = cursor.fetchone()
    print(record)
    print("================================")

    conn.close()
