# File: error_handling_lab.py

filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        print("File content:")
        print(file.read())

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except PermissionError:
    print(f"Error: You do not have permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
