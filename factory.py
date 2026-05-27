#Factory data

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