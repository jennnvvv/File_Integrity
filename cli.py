import argparse
from unittest import result
from checker import create_snapshot, compare_snapshots
from storage import load_db, update_db, save_db
from logger import setup_logger
from alerts import send_alert
from hasher import calculate_hash
import os

logger = setup_logger()

def init(path):
    snapshot = create_snapshot(path)
    update_db(snapshot)
    print("Hashes stored successfully.")
    logger.info("Initialized hashes")


def check(path):
    old_db = load_db()
    new_snapshot = create_snapshot(path)

    result = compare_snapshots(old_db, new_snapshot)

    print("\nScan Results:\n")

    for file in result["modified"]:
        print(f"⚠ Modified: {file}")
        send_alert(f"File modified: {file}")

    for file in result["new"]:
        print(f"➕ New file: {file}")

    for file in result["deleted"]:
        print(f"❌ Deleted: {file}")

    for file in result["unchanged"]:
        print(f"✔ Unchanged: {file}")

    logger.info(f"Scan completed: {result}")
    print("\nSummary:")
    print(f"Modified: {len(result['modified'])}")
    print(f"New: {len(result['new'])}")
    print(f"Deleted: {len(result['deleted'])}")



def update(file_path):
    if not os.path.exists(file_path):
        print("❌ File does not exist.")
        return

    file_path = os.path.abspath(file_path)

    db = load_db()
    file_hash = calculate_hash(file_path)

    db[file_path] = {
        "hash": file_hash
    }

    save_db(db)
    print("Hash updated successfully.")


def run():
    parser = argparse.ArgumentParser(description="File Integrity Checker")

    parser.add_argument("command", choices=["init", "check", "update"])
    parser.add_argument("path", help="File or directory path")

    args = parser.parse_args()

    if args.command == "init":
        init(args.path)
    elif args.command == "check":
        check(args.path)
    elif args.command == "update":
        update(args.path)