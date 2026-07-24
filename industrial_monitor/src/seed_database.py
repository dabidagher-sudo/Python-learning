#Database
from src.service import *
import sqlite3

connection=sqlite3.connect('data/factory.db')
cursor=connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS machine_data
                (
                machine_id TEXT,
                machine_type TEXT,
                status TEXT,
                temp INTEGER,
                pressure INTEGER,
                result TEXT
                )""")

cursor.execute(
    "DELETE FROM machine_data"
)

test_records = [
    ("M01","Machine","RUNNING",28,65,"Ok"),
    ("M02","Machine","RUNNING",35,62,"Temperature Alarm"),
    ("M03","Machine","STOPPED",25,55,"Machine Stopped"),
    ("R01","RobotMachine","RUNNING",45,60,"CRITICAL Temperature Alarm"),
    ("R02","RobotMachine","RUNNING",30,48,"Low Pressure"),
    ("C01","ConveyorMachine","RUNNING",27,70,"Ok"),
    ("P01","PressMachine","STOPPED",32,75,"Machine Stopped"),
    ("P02","PressMachine","RUNNING",29,80,"Ok")
]

for machine in test_records:
    cursor.execute(
        """
        INSERT INTO machine_data(
            machine_id,
            machine_type,
            status,
            temp,
            pressure,
            result
        )

        values(?,?,?,?,?,?)
        """,
        machine
    )

connection.commit()

try:
    cursor.execute(
        "SELECT COUNT(*) FROM machine_data"
    )
    result=cursor.fetchone()[0]
    loginfo_print(f"Test database seeded successfully with {result} records.")
except Exception as e:
    logerror_print(f"Error occurred while counting records: {e}")
connection.close()

