#Factory for database

from machine import Machine
from robot_machine import RobotMachine
from conveyor_machine import ConveyorMachine
from press_machine import PressMachine
from factory import Factory

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
factory.add_machine(conveyor1)
factory.add_machine(conveyor2)
factory.add_machine(robot1)
factory.add_machine(robot2)
factory.add_machine(press1)
factory.add_machine(press2)

return factory