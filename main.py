#Main program

import json
from monitor import read_data, generate_report, save_report, calculate_statistics
from monitor import get_critical_alarms, get_stopped_machines, get_machine_by_id
from monitor import get_running_machines, get_high_temp_machines, get_most_common_alarm
from monitor import calculate_average_temp, get_highest_pressure, count_machine_status, calculate_alarm_percentage
from simulator import simulate
from machine import Machine
from robot_machine import RobotMachine
from conveyor_machine import ConveyorMachine
from press_machine import PressMachine
from factory import Factory

simulate("data.csv", 20)

data= read_data("data.csv")
report= generate_report(data)

for line in report:
    print(line)

save_report("report.txt", report)

avg_temp, avg_pressure, highest_temp, lowest_pressure = calculate_statistics(data)

print("\nProduction Statistics:")
print("Average Temperature: ", round(avg_temp,2))
print("Average Pressure: ", round(avg_pressure,2))
print("Highest Temperature: ", highest_temp)
print("Lowest Pressure: ", lowest_pressure)

with open("machines.json", "r") as file:
    machines= json.load(file)

critical= get_critical_alarms(machines)
print("\nCritical Alarms:")
for machine in critical:
    print(machine)

stopped= get_stopped_machines(machines)
print("\nStopped Machines:")
for machine in stopped:
    print(machine)  

machine_id= "M03"
machine_info= get_machine_by_id(machines, machine_id)
print("\nMachine Search:")
print(machine_info)

running_machines= get_running_machines(machines)
print("\nRunning Machines:")   
for machine in running_machines:
    print(machine)

high_temp_machines= get_high_temp_machines(machines, 40)
print("\nMachines with High Temperature (>40):")
for machine in high_temp_machines:
    print(machine)

avg_temp= calculate_average_temp(machines)
print("\nAverage Temperature of Machines: ", round(avg_temp,2))

highest_pressure= get_highest_pressure(machines)
print("Highest Pressure Recorded: ", highest_pressure)

running, stopped = count_machine_status(machines)
print("\nMachine Status:")
print("Running: ", running)
print("Stopped: ", stopped)

alarm_percentage= calculate_alarm_percentage(machines)
print("\nAlarm Percentage: ", round(alarm_percentage,2), "%")

most_common_alarm= get_most_common_alarm(machines)
print("Most Common Alarm: ", most_common_alarm)

factory= Factory("Main Production Plant")

print("\nMachine Information:")

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

factory.display_factory_status()

robot2.update_values("RUNNING", 42, 65)
conveyor2.update_values("STOPPED", 50, 70)
press2.update_values("RUNNING", 38, 60)

critical= factory.count_critical_alarms()
print("\nCritical Alarms: ", critical)

factory_status= factory.get_factory_status()
print("\nFactory Status: ", factory_status)

factory.display_factory_status()

factory.save_factory("factory_data.json")
