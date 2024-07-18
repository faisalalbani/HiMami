import json
import os

# Path to the JSON file
json_file_path = 'data_user.json'

def load_users():
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            return json.load(file)
    return []

def find_user(email, password):
    users = load_users()
    return next((u for u in users if u["email"] == email and u["password"] == password), None)

def save_user(user):
    users = load_users()
    users.append(user)
    with open(json_file_path, 'w') as file:
        json.dump(users, file, indent=4)

class UMKMModel:
    def __init__(self, filepath="umkm_data.json"):
        self.filepath = filepath

    def save_data(self, data):
        with open(self.filepath, "w") as file:
            json.dump(data, file)

    def load_data(self):
        try:
            with open(self.filepath, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
