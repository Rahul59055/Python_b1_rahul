
import requests

def download_file(url, file_name):
    '''Download a file from the provided URL and save it locally.'''
    
    # Send a GET request to the provided URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open a local file in binary write mode ('wb')
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully")
    else:
        print(f"Failed to download file '{file_name}'")
        print(f"Status code: {response.status_code}")

# To test and debug the code
if __name__ == "__main__":
    url = "https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png"
    download_file(url, "python_logo.png")
    
    
    
    import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to browse and select directory
def browse_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)  # Clear the current directory path
    directory_entry.insert(0, directory)  # Insert the selected directory

# Function to download the file using curl
def download_file():
    url = url_entry.get()
    directory = directory_entry.get()

    if not url or not directory:
        messagebox.showerror("Error", "Please provide both URL and Directory path")
        return

    output_file = os.path.join(directory, url.split("/")[-1])

    # Run curl command
    result = subprocess.run(["curl", "-o", output_file, url])

    if result.returncode == 0:
        messagebox.showinfo("Success", f"File downloaded successfully to {output_file}")
    else:
        messagebox.showerror("Error", "Failed to download file")

# GUI setup
root = tk.Tk()
root.title("File Downloader")

# URL input
tk.Label(root, text="File URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Directory input
tk.Label(root, text="Directory Path:").grid(row=1, column=0, padx=10, pady=10)
directory_entry = tk.Entry(root, width=50)
directory_entry.grid(row=1, column=1, padx=10, pady=10)

# Browse button
browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.grid(row=1, column=2, padx=10, pady=10)

# Download button
download_button = tk.Button(root, text="Download", command=download_file)
download_button.grid(row=2, column=1, pady=10)

root.mainloop()