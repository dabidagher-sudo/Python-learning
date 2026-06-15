#Live monitor
import os
import random
import time
from datetime import datetime

from monitor import analyze_machine

machines= {
    "M01":{}, 
    "M02":{}, 
    "M03":{}, 
    "M04":{}, 
    "M05":{}, 
    "M06":{}
    }
statuses= ["RUNNING", "STOPPED"]

total_alarms= 0
temp_alarms= 0
pressure_alarms= 0
ok_count= 0
total_machines_down=0
critical_alarms=0

while True:
    os.system("cls")
    critical_alarms=0
    total_alarms= 0
    for machine_id in machines:
        status= random.choice(statuses)
        temp= random.randint(20,50)
        pressure= random.randint(30,90)
        timestamp= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result= analyze_machine(status, temp, pressure)

        if status == "STOPPED":
            total_machines_down += 1

        if result == "Temperature Alarm":
            total_alarms += 1
            temp_alarms += 1
        elif result == "CRITICAL Temperature Alarm":
            total_alarms += 1
            critical_alarms += 1
        elif result == "Low Pressure":
            total_alarms += 1
            pressure_alarms +=1
        else:
            ok_count += 1

        machines[machine_id] = {
            "status": status,
            "temp": temp,
            "pressure": pressure,
            "timestamp": timestamp,
            "result": result
        }

    print("=================================")
    print("LIVE MACHINE MONITOR")
    print("=================================")
    for machine_id, data in machines.items():
        print(
            f"{data['timestamp']} |"
            f"{machine_id} | "
            f"{data['status']} | "
            f"Temp: {data['temp']}°C | "
            f"Pressure: {data['pressure']} psi | "
            f"{data['result']} | "
        )
    print("=================================")
    print("Factory Status")
    if critical_alarms > 0:
        print("CRITICAL")
    elif total_alarms > 3:
        print("ALARM")
    else:
        print("NORMAL")        
    print("=================================")
    print(f"Total Alarms: {total_alarms}")
    print(f"Temperature Alarms: {temp_alarms}")
    print(f"Pressure Alarms: {pressure_alarms}")
    print(f"Total Ok: {ok_count}")
    print(f"Total Machines Down: {total_machines_down}")
    print(f"Critical Alarms: {critical_alarms}")
    print("=================================")
    time.sleep(2)
