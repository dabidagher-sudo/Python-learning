#Machine info in class
import time

class Machine:
    def __init__(
            self,
            machine_id,
            status,
            temp,
            pressure,
            machine_type="Machine",
            timestamp=time.strftime("%Y-%m-%d %H:%M:%S")
    ):
        self.machine_id = machine_id
        self.status = status
        self.temp = temp
        self.pressure = pressure
        self.machine_type = machine_type
        self.timestamp = timestamp

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
            f"{self.timestamp}"
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
            "pressure": self.pressure,
            "Timestamp": self.timestamp
        }
    
    def to_db(self):
        return (
            f"{self.machine_id}",
            f"{self.__class__.__name__}",
            f"{self.status}",
            f"{self.temp}",
            f"{self.pressure}",
            f"{self.analyze()}",
            f"{self.timestamp}"
        )