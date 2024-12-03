from tkinter import *
from PIL import ImageTk, Image
import subprocess

def concatenate_strings():
    string1 = text1_input.get()  # Get input from the first text box
    string2 = text2_input.get()  # Get input from the second text box
    result = string1 + string2   # Concatenate the strings
    text2_output.delete(0, END)  # Clear the output box
    text2_output.insert(0, result)  # Insert the result into the output box

def open_main_page():
    root.destroy()  # Close the current window
    subprocess.run(["python", "main_page.py"])  # Open the main page

root = Tk()
root.title('String Concatenation')
root.geometry('700x500')
root.configure(background='#0096DC')

img = Image.open('compiler1.jpg')
resized_img = img.resize((70, 70))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root, image=img)
img_label.pack(pady=(10, 10))

text_label = Label(root, text='Write a Program to Concatenate Two Strings', fg='white', bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana', 20))

# First string input
text1_label = Label(root, text='Enter your First String:', fg='white', bg='#0096DC')
text1_label.pack()
text1_label.config(font=('verdana', 12))
text1_input = Entry(root, width=50)
text1_input.pack(ipady=6, pady=(1, 15))

# Second string input
text2_label = Label(root, text='Enter your Second String:', fg='white', bg='#0096DC')
text2_label.pack()
text2_label.config(font=('verdana', 12))
text2_input = Entry(root, width=50)
text2_input.pack(ipady=6, pady=(1, 15))

# Enter button for concatenation
enter_btn = Button(root, text='Enter', bg='white', fg='black', width=10, height=1, command=concatenate_strings)
enter_btn.pack(pady=(10, 20))
enter_btn.config(font=('verdana', 10))

# Output display
output_label = Label(root, text='Output:', fg='white', bg='#0096DC')
output_label.pack()
output_label.config(font=('verdana', 12))
text2_output = Entry(root, width=50)
text2_output.pack(ipady=6, pady=(1, 15))

# Button to go back to the main page
goto_btn = Button(root, text='Go to Main Page', bg='white', fg='black', width=25, height=1, command=open_main_page)
goto_btn.pack(pady=(10, 20))
goto_btn.config(font=('verdana', 10))

root.mainloop()
