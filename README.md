File Handling
________________________________________
Demonstrate your understanding of Python file handling by completing the following tasks.
Tasks:
1.	File Creation:
•	Create a Python script (file_handling_assignment.py) that does the following:
•	Creates a new text file named "my_file.txt" in write mode ('w').
•	Write at least three lines of text to the file, including a mix of strings and numbers.

1.	File Reading and Display:
•	Enhance your script to read the contents of "my_file.txt" and display them on the console.

1.	File Appending:
•	Modify the script to open "my_file.txt" in append mode ('a').
•	Append three additional lines of text to the existing content.

1.	Error Handling:
•	Implement error handling using try, except, and finally blocks to manage potential file-related exceptions (e.g., FileNotFoundError, PermissionError).


This script defines separate functions for each task:

write_to_file: Takes filename and content as arguments. It uses 'w' mode for writing and handles potential PermissionError and generic exceptions with a try-except-finally block.
read_from_file: Takes filename as an argument. It uses 'r' mode for reading and handles potential FileNotFoundError and generic exceptions.
append_to_file: Takes filename and content as arguments. It uses 'a' mode for appending and handles PermissionError and generic exceptions.
The script demonstrates creating the file, writing content, reading and displaying it, appending additional content, and then reading again to showcase the appended lines.
