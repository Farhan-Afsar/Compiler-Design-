from tkinter import *
from PIL import ImageTk, Image
import subprocess

# Function to tokenize the string
def tokenize_string():
    input_string = text1_input.get()  # Get the input string from the input box

    # Tokenizing the string manually by splitting on spaces
    tokens = []
    word = ""
    for char in input_string:
        if char != " ":  # Collect characters until a space is encountered
            word += char
        else:
            if word:  # Add the word to the tokens list if not empty
                tokens.append(word)
                word = ""
    if word:  # Add the last word if it exists
        tokens.append(word)

    # Display the tokens in the output box
    output_text = "\n".join(tokens)  # Join tokens with newline characters
    text2_output.delete(1.0, END)  # Clear previous output
    text2_output.insert(END, output_text)  # Insert the tokenized result

# Function to go back to the main page (if necessary)
def open_main_page():
    root.destroy()  # Close the current window
    subprocess.run(["python", "main_page.py"])  # Open the main page

# Create the main window
root = Tk()
root.title('String Tokenizer')
root.geometry('700x500')
root.configure(background='#0096DC')

# Optional image for GUI decoration
img = Image.open('compiler2.png')
resized_img = img.resize((70, 70))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root, image=img)
img_label.pack(pady=(10, 10))

# Title label
title_label = Label(root, text='String Tokenizer (Without strtok)', fg='white', bg='#0096DC')
title_label.pack()
title_label.config(font=('verdana', 20))

# Input string label and entry box
input_label = Label(root, text='Enter your String:', fg='white', bg='#0096DC')
input_label.pack()
input_label.config(font=('verdana', 12))

text1_input = Entry(root, width=50)
text1_input.pack(ipady=6, pady=(1, 15))

# Button to tokenize the string
tokenize_btn = Button(root, text='Tokenize', bg='white', fg='black', width=10, height=1, command=tokenize_string)
tokenize_btn.pack(pady=(10, 20))
tokenize_btn.config(font=('verdana', 10))

# Output display label
output_label = Label(root, text='Tokens:', fg='white', bg='#0096DC')
output_label.pack()
output_label.config(font=('verdana', 12))

# Output box to display tokens
text2_output = Text(root, width=50, height=10)
text2_output.pack(pady=(1, 15))

# Button to go back to the main page
goto_btn = Button(root, text='Go to Main Page', bg='white', fg='black', width=25, height=1, command=open_main_page)
goto_btn.pack(pady=(10, 20))
goto_btn.config(font=('verdana', 10))

root.mainloop()
