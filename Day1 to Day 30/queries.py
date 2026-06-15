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
