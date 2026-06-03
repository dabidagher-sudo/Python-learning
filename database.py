#Database
import sqlite3

connection=sqlite3.connect('factory.db')
cursor=connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS machines
                (id INTEGER PRIMARY KEY AUTOINCREMENT,

                machine_id TEXT,
                machine_type TEXT,
                status TEXT,
                temp INTEGER,
                pressure INTEGER,
                result TEXT
                )""")

#connection.commit()


machines=[
    ("M01", "Machine", "RUNNING", 35, 60, "Temperature Alarm"),
    ("R01", "RobotMachine", "RUNNING", 38, 60, "Ok")
]

for machine in machines:
    cursor.execute(
        """
        INSERT INTO machines(
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

cursor.execute(
    "SELECT * FROM machines"
)

rows=cursor.fetchall()

for row in rows:
    print(row)

connection.close()