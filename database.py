#Database
from machine import Machine
from robot_machine import RobotMachine
from conveyor_machine import ConveyorMachine
from press_machine import PressMachine
from factory import Factory
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

factory= Factory("Main Production Plant")

robot1 = RobotMachine("R01", "RUNNING", 38, 60, "Fanuc M20iA")
robot2 = RobotMachine("R02", "STOPPED", 25, 40, "KUKA KR6")
machine1 = Machine("M01", "RUNNING", 35, 60)
machine2 = Machine("M02", "STOPPED", 25, 40)
machine3 = Machine("M03", "RUNNING", 45, 55)
conveyor1 = ConveyorMachine("C01", "RUNNING", 29, 60, 120)
conveyor2 = ConveyorMachine("C02", "RUNNING", 45, 65, 90)
press1 = PressMachine("P01", "RUNNING", 40, 70, 200, 500)
press2 = PressMachine("P02", "STOPPED", 30, 50, 150, 300)

factory.add_machine(machine1)
factory.add_machine(machine2)
factory.add_machine(machine3)
factory.add_machine(robot1)
factory.add_machine(robot2)
factory.add_machine(conveyor1)
factory.add_machine(conveyor2)
factory.add_machine(press1)
factory.add_machine(press2)


machines= factory.get_machines()

factory.display_factory_status()


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