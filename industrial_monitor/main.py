#Main program for industrial monitoring

import json

def load_config(file_name):
    with open(file_name, "r") as file:
        config = json.load(file)

    return config

config = load_config("config.json")

if config["mode"] == "simulation" or config["mode"] == "PLC":
    print ("Industrial Monitor Starting...")
    print("Plant:",config["plant_name"])
    print("Mode:", config["mode"])
    print("Database:", config["database_file"])
    print("Reports:", config["report_folder"])
else:
    print("Invalid mode in config file")