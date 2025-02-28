import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Note: If you encounter a deprecation warning regarding the system version of Tk,
# you can suppress it by setting the environment variable:
# export TK_SILENCE_DEPRECATION=1

def list_files_in_directory():
    # Open a dialog box to select a directory
    directory_path = filedialog.askdirectory()
    
    if directory_path:
        try:
            # List all files in the selected directory
            files = os.listdir(directory_path)
            file_list = "\n".join(files)
            messagebox.showinfo("Files in Directory", f"Files in {directory_path}:\n\n{file_list}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main application window
root = tk.Tk()
root.title("List Files in Directory")

# Create a button to trigger the file listing
browse_button = tk.Button(root, text="Select Folder", command=list_files_in_directory, width=20, height=2)
browse_button.pack(pady=20)

# Run the application
root.mainloop()
