# Service program

from src.logger import *
import os 
import json

def load_config(file_name):
    with open(file_name, "r") as file:
        config = json.load(file)

    return config

def start_aplication():

    log_info("Industrial Monitor Starting")
    config=load_config("config.json")

    log_info("Factory Loaded")

    if config["mode"] == "simulation" or config["mode"] == "PLC":
        print("Industrial Monitor Started")
        print("Plant:",config["plant_name"])
        print("Mode:", config["mode"])
        print("Database:", config["database_file"])
        print("Reports:", config["report_folder"])
    else:
        print("Invalid mode in config file")

    log_info("Program Finished")

    return config

def shutdown_aplication():
    log_info("Industrial Monitor Closed")

def create_folder(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)
        log_info(f"Created folder: {foldername}")
