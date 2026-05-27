#Definitions
import time

def save_event_log(file_name, event_line):
    with open (file_name, "a") as file:
        file.write(event_line + "\n")

def save_daily_summary(file_name, summary_line):
    with open (file_name, "w") as file:
        file.write(summary_line + "\n") 

def save_summary_history(file_name, summary_line):
    with open (file_name, "a") as file:
        file.write(summary_line + "\n")

def analyze_machine(status, temp, pressure):

    if status == "STOPPED":
        return "Machine Stopped"

    if temp>39:
        return "CRITICAL Temperature Alarm"
    elif temp > 30:
        return "Temperature Alarm"
    elif pressure < 50:
        return "Low Pressure"
    else:
        return "Ok"

def read_data(file_name):
    data=[]

    with open (file_name, "r") as file:
        for line in file:
            parts= line.strip().split(",")
            timestamp = parts[0]
            machine_id = parts[1]
            status = parts[2]
            temp = int(parts[3])
            pressure = int(parts[4])
            data.append((timestamp, machine_id, status, temp, pressure))
    
    return data

def generate_report(data):
    total_alarms= 0
    temp_alarms= 0
    pressure_alarms= 0
    ok_count= 0
    total_machines_down=0
    critical_alarms=0
    current_time= time.strftime("%Y-%m-%d %H:%M:%S")

    report_lines= []

    for timestamp, machine_id, status, temp, pressure in data:

        result= analyze_machine(status, temp, pressure)

        report_lines.append(
            f"[{timestamp}] Machine ID= {machine_id}, Status= {status}, temp= {temp}, pressure= {pressure} -> {result}"
        )

        event_line= (
            f"[{timestamp}] Machine= {machine_id}, "
            f"Status={status}, Temp= {temp}, "
            f"Pressure= {pressure}-> {result}"
            )
        save_event_log("machine_events.txt", event_line)

        if status == "STOPPED":
            total_machines_down += 1

        if result == "Temperature Alarm":
            total_alarms += 1
            temp_alarms += 1
        elif result == "CRITICAL Temperature Alarm":
            total_alarms += 1
            critical_alarms += 1
            save_event_log("critical_alarms.txt", event_line)
        elif result == "Low Pressure":
            total_alarms += 1
            pressure_alarms +=1
        else:
            ok_count += 1
    
    report_lines.append("")
    report_lines.append("Summary:")
    report_lines.append(f"Total Alarms: {total_alarms}")
    report_lines.append(f"Temperature Alarms: {temp_alarms}")
    report_lines.append(f"Pressure Alarms: {pressure_alarms}")
    report_lines.append(f"Total Ok: {ok_count}")
    report_lines.append(f"Total Machines Down: {total_machines_down}")
    report_lines.append(f"Critical Alarms: {critical_alarms}")

    summary_line= (
        "***********************************\n"
        f"[{current_time}]\n"
        "Summary:\n"
        f"Total Alarms: {total_alarms}\n"
        f"Temperature Alarms: {temp_alarms}\n"
        f"Pressure Alarms: {pressure_alarms}\n"
        f"Total Ok: {ok_count}\n"
        f"Total Machines Down: {total_machines_down}\n"
        f"Critical Alarms: {critical_alarms}\n"
        "***********************************\n"
    )
    save_daily_summary("daily_summary.txt", summary_line)
    save_summary_history("summary_history.txt", summary_line)

    return report_lines

def save_report(file_name, report_lines):
    with open (file_name, "w") as file:

        for line in report_lines:
            file.write(line + "\n")

def calculate_statistics(data):
    total_temp= 0
    total_pressure= 0
    highest_temp= 0
    lowest_pressure=999

    for timestamp, machine_id, status, temp, pressure in data:
        total_temp += temp
        total_pressure += pressure

        if temp>highest_temp:
            highest_temp= temp
        if pressure<lowest_pressure:
            lowest_pressure=pressure
    
    average_temp= total_temp/ len(data)
    average_pressure= total_pressure/ len(data)

    return average_temp, average_pressure, highest_temp, lowest_pressure

def get_critical_alarms(machines):
    critical_machines= [] 

    for machine in machines:
        if machine["result"] == "CRITICAL Temperature Alarm":
            critical_machines.append(machine)   
    
    return critical_machines

def get_stopped_machines(machines):
    stopped_machines= []

    for machine in machines:
        if machine["status"] == "STOPPED":
            stopped_machines.append(machine)
    
    return stopped_machines

def get_machine_by_id(machines, machine_id):
    for machine in machines:
        if machine["machine_id"] == machine_id:
            return machine
    return None

def get_running_machines(machines):
    running_machines= []

    for machine in machines:
        if machine["status"] == "RUNNING":
            running_machines.append(machine)
    
    return running_machines

def get_high_temp_machines(machines, temp_threshold):
    high_temp_machines= []

    for machine in machines:
        if machine["temp"] > temp_threshold:
            high_temp_machines.append(machine)
    
    return high_temp_machines

def calculate_average_temp(machines):
    total_temp= 0

    for machine in machines:
        total_temp += machine["temp"]
    
    return total_temp/ len(machines) if machines else 0

def get_highest_pressure(machines):
    highest_pressure= 0

    for machine in machines:
        if machine["pressure"] > highest_pressure:
            highest_pressure= machine["pressure"]
    
    return highest_pressure

def count_machine_status(machines):
    running = 0
    stopped = 0
    for machine in machines:
        if machine["status"] == "RUNNING":
            running += 1
        elif machine["status"] == "STOPPED":
            stopped += 1
    
    return running, stopped

def calculate_alarm_percentage(machines):
    alarm_count = 0

    for machine in machines:
        if machine["result"] != "Ok":
            alarm_count += 1
    
    percentage = (alarm_count / len(machines)) * 100 if machines else 0

    return percentage

def get_most_common_alarm(machines):
    alarm_counts = {}

    for machine in machines:
        result = machine["result"]
        if result != "Ok":
            alarm_counts[result] = alarm_counts.get(result, 0) + 1
    
    most_common_alarm = max(alarm_counts, key=alarm_counts.get) if alarm_counts else None

    print (f"Alarm Counts: {alarm_counts}")

    return most_common_alarm
    