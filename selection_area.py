#buttons  that takes you places 
#label 3
#note pad button works

import tkinter as tk
import subprocess

def go_ai():
    subprocess.Popen(['python', 'C:\\Users\\bannw\\Documents\\ella2024softwaredev\\final project\\AIrickroll.py']) # defines values that are set and they will make it easier to open a window. 

def go_writer():
    subprocess.Popen(['python', 'Writerarea.py'])# Popen is a subclass of the subprocess and is not a blocking function unlike the run  function
# referenced or gotten but not copy pasted from https://realpython.com/python-subprocess/#the-popen-class

def go_login():
    subprocess.Popen(['python', 'C:\\Users\\bannw\\Documents\\ella2024softwaredev\\final project\\loginpage.py']) # Popen is basically a run block where it runs a program and then at the end of the program it stops.


root = tk.Tk()
root.title("Program Launcher")

# Create buttons and assign them to functions
button1 = tk.Button(root, text="Login", command=go_login)
button1.pack(pady=10)

button2 = tk.Button(root, text="AI page", command=go_ai)
button2.pack(pady=10)

button3 = tk.Button(root, text="Notepad", command=go_writer)
button3.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()


