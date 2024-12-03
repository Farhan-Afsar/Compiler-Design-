from tkinter import *
from PIL import ImageTk, Image
import subprocess
import re

# Function to identify comments
def identify_comments():
    input_text = text1_input.get("1.0", END).strip()  # Get the input text from the text widget

    # Regex patterns for single-line and multi-line comments
    single_line_pattern = r"//.*"
    multi_line_pattern = r"/\*.*?\*/"

    # Finding comments using regex
    single_line_comments = re.findall(single_line_pattern, input_text)
    multi_line_comments = re.findall(multi_line_pattern, input_text, re.DOTALL)

    # Preparing output
    output_text = ""
    if single_line_comments:
        output_text += "Single-line comment(s):\n" + "\n".join(single_line_comments) + "\n\n"
    else:
        output_text += "No single-line comments found.\n\n"

    if multi_line_comments:
        output_text += "Multi-line comment(s):\n" + "\n".join(multi_line_comments) + "\n"
    else:
        output_text += "No multi-line comments found."

    # Display the results in the output box
    text2_output.delete(1.0, END)  # Clear previous output
    text2_output.insert(END, output_text)  # Insert the results


# Function to go back to the main page
def open_main_page():
    root.destroy()  # Close the current window
    subprocess.run(["python", "main_page.py"])  # Open the main page


# Create the main window
root = Tk()
root.title('Comment Identifier')
root.geometry('700x600')
root.configure(background='#0096DC')

# Optional image for GUI decoration
img = Image.open('compiler2.png')
resized_img = img.resize((70, 70))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root, image=img)
img_label.pack(pady=(10, 10))

# Title label
title_label = Label(root, text='Identify Comments in Input Text', fg='white', bg='#0096DC')
title_label.pack()
title_label.config(font=('verdana', 20))

# Input text label and multi-line text box
input_label = Label(root, text='Enter your Text (Multi-line):', fg='white', bg='#0096DC')
input_label.pack()
input_label.config(font=('verdana', 12))

text1_input = Text(root, width=60, height=10)
text1_input.pack(pady=(1, 15))

# Button to identify comments
identify_btn = Button(root, text='Identify Comments', bg='white', fg='black', width=20, height=1, command=identify_comments)
identify_btn.pack(pady=(10, 20))
identify_btn.config(font=('verdana', 10))

# Output display label
output_label = Label(root, text='Output:', fg='white', bg='#0096DC')
output_label.pack()
output_label.config(font=('verdana', 12))

# Output box to display the results
text2_output = Text(root, width=60, height=10)
text2_output.pack(pady=(1, 15))

# Button to go back to the main page
goto_btn = Button(root, text='Go to Main Page', bg='white', fg='black', width=25, height=1, command=open_main_page)
goto_btn.pack(pady=(10, 20))
goto_btn.config(font=('verdana', 10))

root.mainloop()
