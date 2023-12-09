import tkinter as tk
from tkinter import filedialog
import os
# Create a new Tkinter window
window = tk.Tk()

# Set the window title
window.title("Oprium Desktop App")

# Set the window size
window.geometry("400x300")

# Function to handle file saving
def save_file():
    # Open a file dialog to choose the folder
    folder_path = filedialog.askdirectory()

    # Create a new folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Save the file in the chosen folder
    file_path = os.path.join(folder_path, "example.txt")
    with open(file_path, "w") as file:
        file.write("This is an example file.")

    # Show a message box with the file path
    tk.messagebox.showinfo("File Saved", f"File saved at: {file_path}")

# Create a button to trigger file saving
save_button = tk.Button(window, text="Save File", command=save_file)
save_button.pack()

# Start the Tkinter event loop
window.mainloop()
