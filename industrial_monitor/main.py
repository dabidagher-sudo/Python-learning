#Main program for industrial monitoring

import json
from src.service import *

config = start_aplication()
create_folder("reports")
create_folder("data")
create_folder("logs")

shutdown_aplication()

