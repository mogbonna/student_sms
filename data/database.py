import json
import os

DB_FILE = "data/storage.json"

def load_data():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r') as file:
        return json.load(file)
    
def save_data(data):
    with open(DB_FILE, 'w') as file:
        return json.dump(data, file, indent=4)

# Load data once the module is imported
students_db = load_data() 

# students_db = []