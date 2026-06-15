#Conveyor Machine

from machine import Machine

class ConveyorMachine(Machine):

    pass

    def __init__(
        self,
        machine_id,
        status,
        temp,
        pressure,
        belt_speed,
        machine_type= "ConveyorMachine"
    ):
        super().__init__(
            machine_id,
            status,
            temp,
            pressure,
            machine_type
        )

        self.belt_speed = belt_speed

    def display_info(self):

        result = self.analyze()
        print(
            f"{self.machine_id} | "
            f"Conveyor Speed= {self.belt_speed} m/min | "
            f"{self.status} | "
            f"Temp={self.temp} C | "
            f"Pressure={self.pressure} psi | "
            f"{result}"
        )

    def to_dict(self):
        data = super().to_dict()
        data["belt_speed"] = self.belt_speed 

        return data