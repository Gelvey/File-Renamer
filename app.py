import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def rename_images(folder_path):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']  # Supported image file extensions
    image_count = 1  # Initial image number

    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = os.path.splitext(filename)[1].lower()
            if file_extension in valid_extensions:
                new_filename = f"images{image_count}{file_extension}"
                old_filepath = os.path.join(folder_path, filename)
                new_filepath = os.path.join(folder_path, new_filename)

                # Rename the file
                os.rename(old_filepath, new_filepath)

                # Update image count
                image_count += 1

def select_folder():
    folder_path = filedialog.askdirectory()  # Open folder selection dialog
    if folder_path:
        rename_images(folder_path)
        print("Images renamed successfully!")

# Create the main window
window = tk.Tk()
window.title("Image Renamer")

# Set the window size
window.geometry("400x200")

# Create a button to select a folder
folder_button = tk.Button(window, text="Select Folder", command=select_folder)
folder_button.pack(pady=20)

# Run the main event loop
window.mainloop()