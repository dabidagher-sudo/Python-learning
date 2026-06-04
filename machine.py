#Machine info in class

class Machine:
    def __init__(
            self,
            machine_id,
            status,
            temp,
            pressure,
            machine_type="Machine"
    ):
        self.machine_id = machine_id
        self.status = status
        self.temp = temp
        self.pressure = pressure
        self.machine_type = machine_type

    def analyze(self):
        if self.status == "STOPPED":
            return "Machine Stopped"
        if self.temp > 40:
            return "Critical Temperature Alarm"
        elif self.temp > 30:
            return "Temperature Alarm"
        elif self.pressure < 50:
            return "Low Pressure"
        else:
            return "Ok"
    
    def display_info(self):

        result = self.analyze()
        print(
            f"{self.machine_id} | "
            f"{self.status} | "
            f"Temp={self.temp} C | "
            f"Pressure={self.pressure} psi | "
            f"{result}"
        )
    
    def update_values(self, status, temp, pressure):
        self.status = status
        self.temp = temp
        self.pressure = pressure

    def to_dict(self):
        return {
            "machine_type": self.machine_type,
            "machine_id": self.machine_id,
            "status": self.status,
            "temp": self.temp,
            "pressure": self.pressure
        }
    
    def to_db(self):
        if self.machine_id.startswith("M"):
            type="Machine"
        elif self.machine_id.startswith("R"):
            type="RobotMachine"
        elif self.machine_id.startswith("C"):
            type="ConveyorMachine"
        elif self.machine_id.startswith("P"):
            type="PressMachine"


        return (
            f"{self.machine_id}",
            f"{type}",
            f"{self.status}",
            f"{self.temp}",
            f"{self.pressure}",
            f"{self.analyze()}"
        )