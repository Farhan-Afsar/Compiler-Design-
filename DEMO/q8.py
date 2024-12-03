from tkinter import *
from PIL import ImageTk, Image
import subprocess


# Function to remove special characters
def remove_special_characters():
    input_string = text1_input.get()  # Get the input string from the input box

    # Removing special characters manually
    cleaned_string = ""
    for char in input_string:
        if char.isalnum():  # Check if the character is alphanumeric
            cleaned_string += char

    # Display the cleaned string in the output box
    text2_output.delete(0, END)  # Clear previous output
    text2_output.insert(0, cleaned_string)  # Insert the cleaned string


# Function to go back to the main page
def open_main_page():
    root.destroy()  # Close the current window
    subprocess.run(["python", "main_page.py"])  # Open the main page


# Create the main window
root = Tk()
root.title('Remove Special Characters')
root.geometry('700x500')
root.configure(background='#0096DC')

# Optional image for GUI decoration
img = Image.open('compiler2.png')
resized_img = img.resize((70, 70))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root, image=img)
img_label.pack(pady=(10, 10))

# Title label
title_label = Label(root, text='Remove Special Characters', fg='white', bg='#0096DC')
title_label.pack()
title_label.config(font=('verdana', 20))

# Input string label and entry box
input_label = Label(root, text='Enter your String:', fg='white', bg='#0096DC')
input_label.pack()
input_label.config(font=('verdana', 12))

text1_input = Entry(root, width=50)
text1_input.pack(ipady=6, pady=(1, 15))

# Button to remove special characters
remove_btn = Button(root, text='Remove', bg='white', fg='black', width=10, height=1, command=remove_special_characters)
remove_btn.pack(pady=(10, 20))
remove_btn.config(font=('verdana', 10))

# Output display label
output_label = Label(root, text='Output:', fg='white', bg='#0096DC')
output_label.pack()
output_label.config(font=('verdana', 12))

# Output box to display the cleaned string
text2_output = Entry(root, width=50)
text2_output.pack(ipady=6, pady=(1, 15))

# Button to go back to the main page
goto_btn = Button(root, text='Go to Main Page', bg='white', fg='black', width=25, height=1, command=open_main_page)
goto_btn.pack(pady=(10, 20))
goto_btn.config(font=('verdana', 10))

root.mainloop()
