import json
import os
from datetime import datetime

DB_FILE = "db.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return {}

    with open(DB_FILE, 'r') as f:
        return json.load(f)


def save_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)


def update_db(snapshot):
    db = {}
    for file, file_hash in snapshot.items():
        db[file] = {
            "hash": file_hash,
            "last_checked": str(datetime.now())
        }
    save_db(db)