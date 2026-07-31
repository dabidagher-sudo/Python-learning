#PLC Test
from pylogix import PLC

PLC_IP = "172.16.69.7"

with PLC() as comm:
    comm.IPAddress = PLC_IP

    response = comm.Read("Python_Test")

    print("Value: ", response.Value)
    print("Status: ", response.Status)