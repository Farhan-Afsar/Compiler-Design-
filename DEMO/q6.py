from tkinter import *
from PIL import ImageTk, Image
import subprocess

# Function to count vowels, consonants, and digits
def count_characters():
    input_string = text1_input.get()  # Get the input string
    vowels = "aeiouAEIOU"  # List of vowels
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"  # List of consonants
    digits = "0123456789"  # List of digits

    vowel_count = 0
    consonant_count = 0
    digit_count = 0

    # Iterate through each character in the input string
    for char in input_string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        elif char in digits:
            digit_count += 1

    # Display the results in the output box
    output = f"No of vowels: {vowel_count}\n,No of Consonants: {consonant_count}\n,No of digits: {digit_count}"
    text2_output.delete(0, END)  # Clear previous output
    text2_output.insert(0, output)  # Insert the new result


# Function to go back to the main page (if necessary)
def open_main_page():
    root.destroy()  # Close the current window
    subprocess.run(["python", "main_page.py"])  # Open the main page


root = Tk()
root.title('Character Counter')
root.geometry('700x500')
root.configure(background='#0096DC')

# Image for the GUI (optional, you can adjust the image as needed)
img = Image.open('compiler2.png')
resized_img = img.resize((70, 70))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root, image=img)
img_label.pack(pady=(10, 10))

# Title label
text_label = Label(root, text='Count Vowels, Consonants, and Digits', fg='white', bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana', 20))

# Input string label and entry box
text1_label = Label(root, text='Enter your String:', fg='white', bg='#0096DC')
text1_label.pack()
text1_label.config(font=('verdana', 12))

# Multi-line text box to input the string
text1_input = Entry(root, width=50)
text1_input.pack(ipady=6, pady=(1, 15))

# Enter button to trigger the counting
enter_btn = Button(root, text='Enter', bg='white', fg='black', width=10, height=1, command=count_characters)
enter_btn.pack(pady=(10, 20))
enter_btn.config(font=('verdana', 10))

# Output display
output_label = Label(root, text='Output:', fg='white', bg='#0096DC')
output_label.pack()
output_label.config(font=('verdana', 12))

# Output box to display results
text2_output = Entry(root, width=50)
text2_output.pack(ipady=6, pady=(1, 15))

# Button to go back to the main page
goto_btn = Button(root, text='Go to Main Page', bg='white', fg='black', width=25, height=1, command=open_main_page)
goto_btn.pack(pady=(10, 20))
goto_btn.config(font=('verdana', 10))

root.mainloop()
