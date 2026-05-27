#Factory data

import json
from machine import Machine
from robot_machine import RobotMachine
from conveyor_machine import ConveyorMachine
from press_machine import PressMachine

class Factory:
    def __init__(self,name):
        self.name= name
        self.machines= []

    def add_machine(self, machine):
        self.machines.append(machine)
    
    def display_factory_status(self):
        print("==========================================")
        print(f"FACTORY DASHBOARD: {self.name}")
        print("==========================================")
        for machine in self.machines:
            machine.display_info()
        print("==========================================")

    def count_critical_alarms(self):
        critical_count= 0
        for machine in self.machines:
            result= machine.analyze()
            if result == "Critical Temperature Alarm":
                critical_count += 1
        return critical_count

    def count_stopped_machines(self):
        stopped_count= 0
        for machine in self.machines:
            if machine.status == "STOPPED":
                stopped_count += 1
        return stopped_count

    def get_factory_status(self):
        critical_alarms= self.count_critical_alarms()
        stopped_machines= self.count_stopped_machines()
        if critical_alarms > 0:
            return "CRITICAL"
        elif stopped_machines > 2:
            return "WARNING"
        else:
            return "NORMAL"

    def save_factory(self, filename):
        import json

        factory_data= []
        for machine in self.machines:
            factory_data.append(machine.to_dict())

        with open(filename, "w") as file:
            json.dump(factory_data, file, indent=4)

    def load_factory(self, filename):

        print("\nLoading Machines...")
        with open (filename, "r") as file:
            factory_data= json.load(file)

        self.machines= []
        loaded_count=0

        for machine_data in factory_data:
            machine_type = machine_data["machine_type"]

            if machine_type == "Machine":
                machine= Machine(
                    machine_data["machine_id"],
                    machine_data["status"],
                    machine_data["temp"],
                    machine_data["pressure"]
                )
                loaded_count += 1
            elif machine_type == "RobotMachine":
                machine= RobotMachine(
                    machine_data["machine_id"],
                    machine_data["status"],
                    machine_data["temp"],
                    machine_data["pressure"],
                    machine_data["robot_model"]
                )
                loaded_count += 1
            elif machine_type == "ConveyorMachine":
                machine= ConveyorMachine(
                    machine_data["machine_id"],
                    machine_data["status"],
                    machine_data["temp"],
                    machine_data["pressure"],
                    machine_data["belt_speed"]
                )
                loaded_count += 1
            elif machine_type == "PressMachine":
                machine= PressMachine(
                    machine_data["machine_id"],
                    machine_data['status'],
                    machine_data["temp"],
                    machine_data["pressure"],
                    machine_data["tonnage"],
                    machine_data["hyd_pressure"]
                )
                loaded_count += 1
            else:
                print("Unknown machine type: ", machine_type)

            self.add_machine(machine)
        print("\nLoaded Machines: ", loaded_count)