from tkinter import *
from tkinter import messagebox
import subprocess
import re

# List of C keywords and standard functions to exclude from checks
C_KEYWORDS = {"int", "float", "char", "double", "return", "void", "if", "else", "for", "while", "switch", "case",
              "break", "continue", "default", "sizeof", "long", "short", "printf", "scanf", "main", "include", "const",
              "static", "struct", "union", "enum"}


# Function to check for errors in the C program
def check_c_program():
    input_code = text_input.get("1.0", END).strip()  # Get the C program input

    # Error tracking
    errors = []

    # Check for unmatched braces or parentheses
    if input_code.count("{") != input_code.count("}"):
        errors.append("Mismatched braces: '{' and '}' are not balanced.")
    if input_code.count("(") != input_code.count(")"):
        errors.append("Mismatched parentheses: '(' and ')' are not balanced.")

    # Check for missing semicolons, ignoring function headers, braces, and comments
    lines = input_code.split("\n")
    for i, line in enumerate(lines, start=1):
        stripped_line = line.strip()

        # Ignore lines that don't require semicolons
        if (stripped_line.endswith("{") or
                stripped_line.endswith("}") or
                stripped_line.startswith("//") or
                stripped_line.startswith("/*") or
                stripped_line.startswith("#") or
                stripped_line == ""):
            continue

        # Check if a statement requires a semicolon but doesn't end with one
        if not stripped_line.endswith(";") and not stripped_line.endswith("*/"):
            errors.append(f"Missing semicolon at line {i}: {line}")

    # Regular expression to find undeclared variables (e.g., b in your code)
    declared_variables = set()
    for line in input_code.split("\n"):
        # Match variable declarations (e.g., int a; or float x;)
        match = re.match(r"\s*(int|float|char|double)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*;", line.strip())
        if match:
            declared_variables.add(match.group(2))

    # Check for usage of undeclared variables
    for i, line in enumerate(lines, start=1):
        words = re.findall(r"\b[a-zA-Z_][a-zA-Z0-9_]*\b", line.strip())  # Match all variable-like words
        for word in words:
            # Ignore C keywords and function names
            if word not in declared_variables and word not in C_KEYWORDS:
                errors.append(f"Undeclared variable '{word}' at line {i}: {line}")

    # Display results
    if errors:
        result_label.config(text="Rejected", fg="red")
        output_text.delete(1.0, END)
        output_text.insert(END, "Errors Found:\n" + "\n".join(errors))
    else:
        result_label.config(text="Accepted", fg="green")
        output_text.delete(1.0, END)
        output_text.insert(END, "No errors found. Code Accepted.")


# Function to go back to the main page
def open_main_page():
    root.destroy()  # Close the current window
    subprocess.run(["python", "main_page.py"])  # Open the main page


# Create the main window
root = Tk()
root.title("C Program Mini Compiler")
root.geometry("800x600")
root.configure(background="#0096DC")

# Title label
title_label = Label(root, text="C Program Mini Compiler", fg="white", bg="#0096DC")
title_label.pack(pady=10)
title_label.config(font=("verdana", 20))

# Input label and multi-line text box for the C program
input_label = Label(root, text="Enter your C Program:", fg="white", bg="#0096DC")
input_label.pack()
input_label.config(font=("verdana", 12))

text_input = Text(root, width=80, height=15)
text_input.pack(pady=(5, 15))

# Button to check the C program
check_btn = Button(root, text="Check Program", bg="white", fg="black", width=15, height=1, command=check_c_program)
check_btn.pack(pady=(10, 20))
check_btn.config(font=("verdana", 10))

# Result label to display Accepted/Rejected
result_label = Label(root, text="", fg="black", bg="#0096DC")
result_label.pack(pady=(5, 10))
result_label.config(font=("verdana", 15))

# Output text box to display errors or success message
output_text = Text(root, width=80, height=10)
output_text.pack(pady=(5, 15))

# Button to go back to the main page
goto_btn = Button(root, text="Go to Main Page", bg="white", fg="black", width=25, height=1, command=open_main_page)
goto_btn.pack(pady=(10, 20))
goto_btn.config(font=("verdana", 10))

root.mainloop()
