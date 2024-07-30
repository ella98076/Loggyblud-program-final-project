
"""_summary_
    used as a joke, since it has to be fun. But after your done just click the x button at the top of the window. 
    """

import tkinter as tk
from tkinter import ttk
import os

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Ai r")

    # Specify the path to the image
    image_path = "rickroll_4k.png"  # Path to the uploaded PNG image
    if not os.path.exists(image_path):
        print(f"Image file '{image_path}' not found")
        return


    photo = tk.PhotoImage(file=image_path) # gets image into existence 

    # creates canvas to hold text & photo
    canvas = tk.Canvas(root, width=photo.width(), height=photo.height())
    canvas.pack()

    #adds image into universe 
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

    
    canvas.create_text(photo.width() // 2, photo.height() // 2, text=" Never gonna give you up! never gonna let you down! #rickroll", fill="white", font=("Helvetica", 24, "bold")) # creates & adds text

   # ensures image is not trash
    canvas.image = photo

    # start window loop
    root.mainloop()

if __name__ == "__main__":
    main()
    
# code referenced from google & https://www.geeksforgeeks.org/creating-a-labelframe-inside-a-tkinter-canvas/
