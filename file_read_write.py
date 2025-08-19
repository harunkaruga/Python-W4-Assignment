# File: file_read_write.py

# Define the input and output filenames
input_file = "original.txt"
output_file = "modified.txt"

try:
    # Open the original file in read mode
    with open(input_file, "r") as file:
        content = file.readlines()

    # Modify the content (example: make all text uppercase)
    modified_content = [line.upper() for line in content]

    # Write modified content to a new file
    with open(output_file, "w") as file:
        file.writelines(modified_content)

    print(f"Modified content written to {output_file} successfully!")

except FileNotFoundError:
    print(f"Error: The file '{input_file}' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
