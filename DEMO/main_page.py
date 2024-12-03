from tkinter import *
from PIL import ImageTk, Image
import subprocess


def open_q1():
    root.destroy()  # Close the current window
    subprocess.run(["python", "q1.py"])  # Open the other page

def open_q2():
    root.destroy()  # Close the current window
    subprocess.run(["python", "q2.py"])  # Open the other page

def open_q3():
    root.destroy()  # Close the current window
    subprocess.run(["python", "q3.py"])  # Open the other page

def open_q4():
    root.destroy()  # Close the current window
    subprocess.run(["python", "q4.py"])  # Open the other page

def open_q5():
    root.destroy()  # Close the current window
    subprocess.run(["python", "q5.py"])  # Open the other page
def open_q6():
    root.destroy()  # Close the current window
    subprocess.run(["python", "q6.py"])  # Open the other page
def open_q7():
    root.destroy()  # Close the current window
    subprocess.run(["python", "q7.py"])  # Open the other page

def open_q8():
    root.destroy()  # Close the current window
    subprocess.run(["python", "q8.py"])  # Open the other page

def open_q9():
    root.destroy()  # Close the current window
    subprocess.run(["python", "q9.py"])  # Open the other page

def open_q10():
    root.destroy()  # Close the current window
    subprocess.run(["python", "q10.py"])  # Open the other page

root = Tk()
root.title('Main Page')
root.geometry('1116x800')
root.configure(background='#2C3E50')  # Dark background for a modern look

# Load the image
img = Image.open('compiler2.png')  # Make sure the image is available
resized_img = img.resize((100, 100))  # Resize for prominence
img = ImageTk.PhotoImage(resized_img)

# Display the image
img_label = Label(root, image=img, bg='#2C3E50')
img_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

# Main title label
text_label = Label(root, text='The Problems...', fg='#ECF0F1', bg='#2C3E50')
text_label.grid(row=1, column=0, columnspan=2, pady=(10, 10))
text_label.config(font=('Arial', 30, 'bold'))

# Function to create question buttons
def create_button(question_text, command, row):
    question_label = Label(root, text=question_text, fg='#ECF0F1', bg='#2C3E50', anchor="w")
    question_label.grid(row=row, column=0, padx=(20, 0), pady=(10, 5), sticky='w')
    question_label.config(font=('Verdana', 14))

    button = Button(root, text='Go for solutions...', bg='#3498DB', fg='white', width=25, height=2, command=command, relief='flat')
    button.grid(row=row, column=1, padx=(10, 20), pady=(5, 20))
    button.config(font=('Verdana', 12))


# Create question buttons with respective functions
create_button('1. Write a Program to concatenate two strings.', open_q1, 2)
create_button('2. Write a Program to Scan and Count the number of characters, words, and lines', open_q2, 3)
create_button('3. Write a Program that accepts a+', open_q3, 4)
create_button('4. Write a Program that accepts a*b.', open_q4, 5)
create_button('5. Write a Program to remove white spaces from a string.', open_q5, 6)
create_button(question_text='6. Write a  program that will count vowel, consonant & digit of a given string.',command=open_q6, row=7)
create_button('7. Write a Program to tokenize the string.', open_q7, 8)
create_button('8. Write a Program to remove special characters', open_q8, 9)
create_button('9. Write a Program to count the articles', open_q9, 10)
create_button('10. Write a Program to identify comments', open_q10, 11)

# Bottom spacer
spacer_bottom = Label(root, text="", bg='#2C3E50')
spacer_bottom.grid(row=7, column=0, columnspan=2, pady=20)

# Run the Tkinter event loop
root.mainloop()
