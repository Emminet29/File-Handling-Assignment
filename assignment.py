
#File Creation:
#Create a Python script (file_handling_assignment.py) that does the following:
#Creates a new text file named "my_file.txt" in write mode ('w').
#Write at least three lines of text to the file, including a mix of strings and numbers.

# For File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is line 1.\n")
        file.write("12345 is a number.\n")
        file.write("File handling assignment in Python.\n")

    print("File creation and initial writing completed.")

except FileNotFoundError as e:
    print(f"Error: {e}. Check if the file path is correct.")

except PermissionError as e:
    print(f"Error: {e}. Ensure you have the necessary permissions to write to the file.")

finally:
    print("File Creation Task Completed.\n")


#File Reading and Display:
#Enhance your script to read the contents of "my_file.txt" and display them on the console.


# For File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("File Content:\n", content)

except FileNotFoundError as e:
    print(f"Error: {e}. The file does not exist.")

except PermissionError as e:
    print(f"Error: {e}. Ensure you have the necessary permissions to read the file.")

finally:
    print("File Reading Task Completed.\n")


#File Appending:
#Modify the script to open "my_file.txt" in append mode ('a').
#Append three additional lines of text to the existing content.


# For File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending a new line.\n")
        file.write("Additional content for the file.\n")
        file.write("Python file handling is interesting.\n")

    print("File appending completed.")

    #Error Handling:
    #Implement error handling using try, except, and finally blocks to manage potential file-related exceptions (e.g., FileNotFoundError, PermissionError).

except FileNotFoundError as e:
    print(f"Error: {e}. The file does not exist.")

except PermissionError as e:
    print(f"Error: {e}. Ensure you have the necessary permissions to append to the file.")

finally:
    print("File Appending Task Completed.\n")
