# Service program

from src.logger import *
import os 
import json

def load_config(file_name):
    with open(file_name, "r") as file:
        config = json.load(file)

    return config

def loginfo_print(message):
    print(message)
    log_info(message)

def logerror_print(message):
    print(message)
    log_error(message)

def create_folder(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)
        log_info(f"Created folder: {foldername}")

def start_aplication():

    create_folder("reports")
    create_folder("data")
    create_folder("logs")
    loginfo_print("Industrial Monitor Starting")
    config=load_config("config.json")

    loginfo_print("Factory Loaded")

    if config["mode"] == "simulation" or config["mode"] == "PLC":
        print("Plant:",config["plant_name"])
        print("Mode:", config["mode"])
        print("Database:", config["database_file"])
        print("Reports:", config["report_folder"])
    else:
        print("Invalid mode in config file")

    loginfo_print("Program Finished")

    return config

def shutdown_aplication():
    loginfo_print("Industrial Monitor Closed")


