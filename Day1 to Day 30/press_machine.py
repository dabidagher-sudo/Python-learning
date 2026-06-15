#Press Machine

from machine import Machine

class PressMachine(Machine):

    pass

    def __init__(
        self,
        machine_id,
        status,
        temp,
        pressure,
        hyd_pressure,
        tonnage,
        machine_type= "PressMachine"
    ):
        super().__init__(
            machine_id,
            status,
            temp,
            pressure,
            machine_type
        )

        self.tonnage = tonnage
        self.hyd_pressure = hyd_pressure

    def display_info(self):

        result = self.analyze()
        print(
            f"{self.machine_id} | "
            f"Tonnage= {self.tonnage} tons | "
            f"{self.status} | "
            f"Temp={self.temp} C | "
            f"Pressure={self.pressure} psi | "
            f"Hydraulic Pressure={self.hyd_pressure} psi | "
            f"{result}"
        )

    def to_dict(self):
        data = super().to_dict()
        data["tonnage"] = self.tonnage 
        data["hyd_pressure"] = (self.hyd_pressure)

        return data