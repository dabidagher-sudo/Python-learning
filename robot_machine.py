#Robot machine

from machine import Machine

class RobotMachine(Machine):

    pass

    def __init__(
        self,
        machine_id,
        status,
        temp,
        pressure,
        robot_model,
        machine_type= "RobotMachine"
    ):
        super().__init__(
            machine_id,
            status,
            temp,
            pressure,
            machine_type
        )

        self.robot_model = robot_model

    def display_info(self):

        result = self.analyze()
        print(
            f"{self.machine_id} | "
            f"Robot= {self.robot_model} | "
            f"{self.status} | "
            f"Temp={self.temp} C | "
            f"Pressure={self.pressure} psi | "
            f"{result}"
        )
    
    def to_dict(self):
        data = super().to_dict()
        data["robot_model"] = self.robot_model 

        return data


