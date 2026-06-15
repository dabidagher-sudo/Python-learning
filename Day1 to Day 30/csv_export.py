# CSV Export data from Factory to CSV file

import csv

def export_factory_data(factory, filename):
    factory_data= factory.get_machines()
    with open(filename, "w", newline="") as file:
        write = csv.writer(file)
        write.writerow(
            [
                "machine_id",
                "machine_type",
                "status",
                "temp",
                "pressure",
                "result",
                "timestamp"
            ]
        )
        for machine in factory_data:
            write.writerow(machine)
    
    print ("CSV Export Completed.")

def export_alarms_only(factory, filename):
    factory_data= factory.get_alarms_only()
    
    with open(filename,"w", newline="") as file:
        write = csv.writer(file)
        write.writerow(
            [
                "machine_id",
                "machine_type",
                "status",
                "temp",
                "pressure",
                "result",
                "timestamp"
            ]
        )
        for machine in factory_data:
            write.writerow(machine)
    
    print("Alarms Only CSV Export Completed.")