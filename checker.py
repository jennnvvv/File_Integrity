import os
from hasher import calculate_hash

IGNORE = ['.git', '__pycache__', 'logs', 'db.json']
def should_ignore(file_path):
    ignore_files = ['db.json']
    ignore_dirs = ['.git', '__pycache__', 'logs']

    for d in ignore_dirs:
        if d in file_path:
            return True

    for f in ignore_files:
        if file_path.endswith(f):
            return True

    return False



def scan_directory(path):
    files = []

    if os.path.isfile(path):
        return [os.path.abspath(path)]

    for root, _, filenames in os.walk(path):
        for file in filenames:
            full_path = os.path.abspath(os.path.join(root, file))

            if should_ignore(full_path):
                continue

            files.append(full_path)

    return files


def create_snapshot(path):
    snapshot = {}
    files = scan_directory(path)

    for file in files:
        normalized_path = os.path.abspath(file)
        file_hash = calculate_hash(normalized_path)

        if file_hash:
            snapshot[normalized_path] = file_hash

    return snapshot


def compare_snapshots(old_db, new_snapshot):
    result = {
        "modified": [],
        "new": [],
        "deleted": [],
        "unchanged": []
    }

    old_files = set(old_db.keys())
    new_files = set(new_snapshot.keys())

    for file in new_files:
        if file not in old_files:
            result["new"].append(file)
        elif old_db[file]["hash"] != new_snapshot[file]:
            result["modified"].append(file)
        else:
            result["unchanged"].append(file)

    for file in old_files:
        if file not in new_files:
            result["deleted"].append(file)

    return result
