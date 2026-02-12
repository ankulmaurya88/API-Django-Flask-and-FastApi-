import json
import os
DB_FILE_PATH = os.path.join("data", "data_storage.json")

JSON_FILE = "data/users.json"

def load_from_disk():
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, "r") as f:
        return json.load(f)


def sync_to_disk():
    """Helper function to save the current normal_data list to a file"""
    with open(DB_FILE_PATH, "w") as f:
        json.dump(normal_data, f, indent=4)


def save_to_disk(data_list):
    with open(JSON_FILE, "w") as f:
        json.dump(data_list, f, indent=4)


key_value_data={}

normal_data=[]

unquine_data=set()

normal_data = load_from_disk()