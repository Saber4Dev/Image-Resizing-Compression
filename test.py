import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

# Create the main window
window = tk.Tk()
window.title("Image Resizing & Compression")
window.geometry("500x400")

# Variables
image_paths = []
crop_var = tk.BooleanVar()
compress_var = tk.BooleanVar()

# Function to handle image selection
def select_images():
    image_paths.clear()
    filetypes = (("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*"))
    selected_files = filedialog.askopenfilenames(filetypes=filetypes)
    image_paths.extend(selected_files)

# Function to process the images
def process_images():
    if len(image_paths) == 0:
        messagebox.showwarning("Warning", "No images selected.")
        return
    
    for image_path in image_paths:
        try:
            img = Image.open(image_path)

            # Resize the image
            if crop_var.get():
                width = int(size_entry.get())
                height = int(size_entry.get())
                resized_img = img.resize((width, height))
                resized_img.thumbnail((width, height), Image.ANTIALIAS)
            else:
                width = int(size_entry.get())
                height = int(size_entry.get())
                resized_img = img.resize((width, height))

            # Compress the image
            if compress_var.get():
                resized_img.save("Export/compressed_" + image_path.split("/")[-1], optimize=True, quality=70)
            else:
                resized_img.save("Export/" + image_path.split("/")[-1])

        except Exception as e:
            messagebox.showerror("Error", str(e))
            return
    
    messagebox.showinfo("Success", "Image processing complete.")

# Image Selection Frame
drop_frame = tk.Frame(window)
drop_frame.pack(pady=20)

drop_label = tk.Label(drop_frame, text="Drag and Drop Images Here")
drop_label.pack()

# Resize Options Frame
resize_frame = tk.Frame(window)
resize_frame.pack(pady=20)

size_label = tk.Label(resize_frame, text="Size:")
size_label.grid(row=0, column=0, padx=10)

size_entry = tk.Entry(resize_frame)
size_entry.grid(row=0, column=1, padx=10)

# Crop Checkbox
crop_checkbox = tk.Checkbutton(window, text="Crop", variable=crop_var)
crop_checkbox.pack()

# Compress Checkbox
compress_checkbox = tk.Checkbutton(window, text="Compress", variable=compress_var)
compress_checkbox.pack()

# Process Images Button
process_button = tk.Button(window, text="Process Images", command=process_images)
process_button.pack(pady=20)

# Status Label
status_label = tk.Label(window, text="")
status_label.pack()

# Main loop
window.mainloop()
