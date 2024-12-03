from tkinter import *
from PIL import ImageTk, Image
import subprocess


# Function to calculate and display the results
def result():
    input_text = text1_input.get("1.0", END).strip()  # Get text from the Text widget
    if input_text:  # Check if input is not empty
        lines = input_text.splitlines()  # Split into lines
        num_lines = len(lines)  # Count lines
        num_words = sum(len(line.split()) for line in lines)  # Count words
        num_characters = sum(len(line) for line in lines)  # Count characters

        # Format and display the result
        output = f"Lines: {num_lines}, Words: {num_words}, Characters: {num_characters}"
    else:
        output = "Please enter a valid string!"

    # Display the output in the output box
    text2_output.delete(0, END)  # Clear the output box
    text2_output.insert(0, output)  # Insert the result


# Function to navigate back to the main page
def open_main_page():
    root.destroy()  # Close the current window
    subprocess.run(["python", "main_page.py"])  # Open the main page


root = Tk()
root.title('Text Scanner')
root.geometry('700x600')
root.configure(background='#0096DC')

# Image
img = Image.open('compiler1.jpg')
resized_img = img.resize((70, 70))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root, image=img)
img_label.pack(pady=(10, 10))

# Title Label
text_label = Label(root, text='Scan and Count: Characters, Words, and Lines', fg='white', bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana', 18))

# Input String Label and Multi-Line Text Box
text1_label = Label(root, text='Enter your String:', fg='white', bg='#0096DC')
text1_label.pack()
text1_label.config(font=('verdana', 12))
text1_input = Text(root, width=60, height=10, wrap=WORD)
text1_input.pack(pady=(1, 15))

# Enter Button
enter_btn = Button(root, text='Enter', bg='white', fg='black', width=10, height=1, command=result)
enter_btn.pack(pady=(10, 20))
enter_btn.config(font=('verdana', 10))

# Output Label and Entry Box
output_label = Label(root, text='Output:', fg='white', bg='#0096DC')
output_label.pack()
output_label.config(font=('verdana', 12))
text2_output = Entry(root, width=50)
text2_output.pack(ipady=6, pady=(1, 15))

# Go to Main Page Button
goto_btn = Button(root, text='Go to Main Page', bg='white', fg='black', width=25, height=1, command=open_main_page)
goto_btn.pack(pady=(10, 20))
goto_btn.config(font=('verdana', 10))

root.mainloop()
