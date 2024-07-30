
"""
this program is to give the user a place to log in. This is used as a start screen for a website or a application. 
If you use numbers in your username it will decline you and you will see a pop-up window stating that you can't use numbers in your username.
"""
import tkinter as tk
import subprocess

# Function to handle login button click
def login():
    user_input = text_box.get()
    if user_input.isalpha():
        open_selection_page()
    else:
        messagebox.showerror("Invalid Input", "Please enter only alphabetical values.")

# Function to open the pre-existing file for the selection page

def go_select():
    try:
        subprocess.Popen(['python', 'C:\\Users\\bannw\\Documents\\ella2024softwaredev\\final project\\selection_area.py'])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open selection page program: {e}")
        # has try button to try to go to selection window , incase file isn't there would be an error showing.

# Main window
window2 = tk.Tk()
window2.geometry('700x700')
window2.title('Login Page')
window2.config(background='#F3F3F3')

# Login button
button_login = tk.Button(
    text="Login",
    width=25,
    height=2,
    bg="light grey",
    fg="black",
    command= go_select
)

# Text box for user input
text_box = tk.Entry(
    window2,
    width=50,
    bg="white",
    fg="black"
)

# Configure grid layout
for i in range(7):
    window2.columnconfigure(i, weight=1)
    window2.rowconfigure(i, weight=i+1)

# Place widgets in the grid
text_box.grid(row=4, column=2)
button_login.grid(row=4, column=3)

# Run the Tkinter event loop
window2.mainloop()
