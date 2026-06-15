#Simulator
import random
import time

def simulate(data_file, num_entries):
    stored_data = []
    machine_ids= ["M01", "M02", "M03", "M04", "M05", "M06"]
    statuses= ["RUNNING", "STOPPED"]
    
    for _ in range(num_entries):
        machine_id= random.choice(machine_ids)
        status= random.choice(statuses)
        temp= random.randint(20,50)
        pressure= random.randint(40,90)
        timestamp= time.strftime("%Y-%m-%d %H:%M:%S")

        stored_data.append((timestamp, machine_id, status, temp, pressure))
    
    with open(data_file, "w") as file:
        for entry in stored_data:
            line= ",".join(map(str, entry))
            file.write(line + "\n")





