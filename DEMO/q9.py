from tkinter import *
from PIL import ImageTk, Image
import subprocess


# Function to count the articles
def count_articles():
    input_string = text1_input.get()  # Get the input string from the input box
    words = input_string.split()  # Split the input string into words

    # Initialize counts for articles
    count_a = words.count('a')
    count_an = words.count('an')
    count_the = words.count('the')

    # Display the results in the output box
    output_text = f"Count of 'a': {count_a}\nCount of 'an': {count_an}\nCount of 'the': {count_the}"
    text2_output.delete(1.0, END)  # Clear previous output
    text2_output.insert(END, output_text)  # Insert the article counts


# Function to go back to the main page
def open_main_page():
    root.destroy()  # Close the current window
    subprocess.run(["python", "main_page.py"])  # Open the main page


# Create the main window
root = Tk()
root.title('Article Counter')
root.geometry('700x500')
root.configure(background='#0096DC')

# Optional image for GUI decoration
img = Image.open('compiler2.png')
resized_img = img.resize((70, 70))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root, image=img)
img_label.pack(pady=(10, 10))

# Title label
title_label = Label(root, text='Count Articles in a String', fg='white', bg='#0096DC')
title_label.pack()
title_label.config(font=('verdana', 20))

# Input string label and entry box
input_label = Label(root, text='Enter your String:', fg='white', bg='#0096DC')
input_label.pack()
input_label.config(font=('verdana', 12))

text1_input = Entry(root, width=50)
text1_input.pack(ipady=6, pady=(1, 15))

# Button to count articles
count_btn = Button(root, text='Count Articles', bg='white', fg='black', width=15, height=1, command=count_articles)
count_btn.pack(pady=(10, 20))
count_btn.config(font=('verdana', 10))

# Output display label
output_label = Label(root, text='Output:', fg='white', bg='#0096DC')
output_label.pack()
output_label.config(font=('verdana', 12))

# Output box to display the results
text2_output = Text(root, width=40, height=7)
text2_output.pack(pady=(1, 15))

# Button to go back to the main page
goto_btn = Button(root, text='Go to Main Page', bg='white', fg='black', width=25, height=1, command=open_main_page)
goto_btn.pack(pady=(10, 20))
goto_btn.config(font=('verdana', 10))

root.mainloop()
