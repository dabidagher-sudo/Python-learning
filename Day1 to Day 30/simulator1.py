#JSON files

import random
import time
import json
from monitor import analyze_machine

stored_data = []
critical_alarm_data = []
machine_ids= ["M01", "M02", "M03", "M04", "M05", "M06"]
statuses= ["RUNNING", "STOPPED"]
    
for _ in range(10):

    machine_id= random.choice(machine_ids)
    status= random.choice(statuses)
    temp= random.randint(20,50)
    pressure= random.randint(40,90)
    timestamp= time.strftime("%Y-%m-%d %H:%M:%S")
    result= analyze_machine(status, temp, pressure)

    machine_data = {
        "timestamp": timestamp,
        "machine_id": machine_id,
        "status": status,
        "temp": temp,
        "pressure": pressure,
        "result": result
    }

    stored_data.append(machine_data)
    if result == "CRITICAL Temperature Alarm":
        critical_alarm_data.append(machine_data)


with open("machines.json", "w") as file:
    json.dump(stored_data, file, indent=4) 
    
with open("critical_alarms.json", "w") as file:
   json.dump(critical_alarm_data, file, indent=4)
