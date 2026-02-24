import hashlib
import json
import os

def generate_checksum(file_path):
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def lock_file(file_path):
    checksum = generate_checksum(file_path)

    lock_data = {
        "file": file_path,
        "checksum": checksum,
        "status": "MASTER_LOCK"
    }

    with open(file_path + ".lock", "w") as f:
        json.dump(lock_data, f, indent=4)

    print("File locked successfully.")

def verify_lock(file_path):
    lock_file_path = file_path + ".lock"

    if not os.path.exists(lock_file_path):
        return True

    with open(lock_file_path, "r") as f:
        lock_data = json.load(f)

    current_checksum = generate_checksum(file_path)

    if current_checksum != lock_data["checksum"]:
        print("ERROR: File integrity violation detected.")
        return False

    return True