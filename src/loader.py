import json

FILE_PATH = "src/data/user_data.json"

def load_data():
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_data(data):

    existing_data = load_data()

    existing_data.append(data)

    with open(FILE_PATH, "w") as f:
        json.dump(existing_data, f, indent=4)