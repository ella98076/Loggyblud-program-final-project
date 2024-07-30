# expandable text box 
# save the work
# able to change the font and etc.
# able to name title 
# use labelEntry for this since its like a entry box or like a notepad. 
# label 1 

import tkinter as tk
from tkinter import ttk

# Create the main application window
class NotepadApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the window size and title
        self.geometry('700x700')
        self.title('Notepad')

        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Add a label with directions
        directions = tk.Label(self, text="Welcome to the notepad side of things, click the text box to enter text.", font=("Arial", 14))
        directions.grid(row=0, column=0, padx=8, pady=10, sticky="nsew")

        # Add an expandable text box
        self.text_box = tk.Text(self, wrap='word', font=("Arial", 12))
        self.text_box.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Run the application
if __name__ == "__main__":
    app = NotepadApp()
    app.mainloop()
