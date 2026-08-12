import hashlib
import os

def calculate_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


filename = input("Enter the file path: ")

if os.path.exists(filename):
    file_hash = calculate_hash(filename)

    print("\nSHA-256 Hash:")
    print(file_hash)
else:
    print("File not found.")
