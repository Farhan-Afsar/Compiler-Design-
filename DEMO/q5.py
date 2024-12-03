from tkinter import *
from PIL import ImageTk, Image
import subprocess
# Function to remove spaces from the string
def remove_whitespace():
    input_text = text1_input.get("1.0", END).strip()  # Get text from the Text widget
    if input_text:  # Check if input is not empty
        # Remove all spaces from the string
        output_text = input_text.replace(" ", "")
    else:
        output_text = "Please enter a valid string!"

    # Display the output in the output box
    text2_output.delete(0, END)  # Clear the output box
    text2_output.insert(0, output_text)  # Insert the result


# Function to navigate back to the main page
def open_main_page():
    root.destroy()  # Close the current window
    subprocess.run(["python", "main_page.py"])  # Open the main page


root = Tk()
root.title('Remove White Spaces')
root.geometry('700x600')
root.configure(background='#0096DC')

# Image (replace with your image file path)
img = Image.open('compiler1.jpg')  # Replace with your image file
resized_img = img.resize((70, 70))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root, image=img)
img_label.pack(pady=(10, 10))

# Title Label
text_label = Label(root, text='Remove White Spaces from String', fg='white', bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana', 18))

# Input String Label and Multi-Line Text Box
text1_label = Label(root, text='Enter your String:', fg='white', bg='#0096DC')
text1_label.pack()
text1_label.config(font=('verdana', 12))
text1_input = Text(root, width=60, height=10, wrap=WORD)
text1_input.pack(pady=(1, 15))

# Enter Button to remove whitespaces
enter_btn = Button(root, text='Remove Whitespace', bg='white', fg='black', width=15, height=1, command=remove_whitespace)
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
