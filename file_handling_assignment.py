# Here's the Python script demonstrating file handling with error handling:

def write_to_file(filename, content):
      #Writes content to a file in write mode.
      #filename: The name of the file to write to.
      #content: The content to be written.
  try:
    with open(filename, 'w') as file:
      if isinstance(content, list):
        file.writelines(content)
      else:
        file.write(content)
  except PermissionError:
    print("Error: Insufficient permission to write to the file.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
  finally:
    print(f"Successfully wrote to {filename}.")

def read_from_file(filename):
    #Reads the contents of a file and displays them on the console.
    #filename: The name of the file to read from.
  try:
    with open(filename, 'r') as file:
      content = file.read()
      print(content)
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
  finally:
    print(f"Finished reading {filename}.")

def append_to_file(filename, content):
    #Appends content to a file in append mode.
    #filename: The name of the file to append to.
    #content: The content to be appended.
  try:
    with open(filename, 'a') as file:
      if isinstance(content, list):
        file.writelines(content)
      else:
        file.write(content + "\n")
  except PermissionError:
    print("Error: Insufficient permission to append to the file.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
  finally:
    print(f"Successfully appended to {filename}.")

# File Creation
write_to_file("my_file.txt", ["This is the first line.\n", "This line has a number: 42\n", "Here's some more text.\n"])

# File Reading and Display
read_from_file("my_file.txt")

# File Appending
append_to_file("my_file.txt", ["Line to be appended 1\n", "Line to be appended 2\n", "Line to be appended 3\n"])

# Read again to see the appended content
read_from_file("my_file.txt")