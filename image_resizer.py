from tkinter import Tk, Button, Label, filedialog, Canvas, Frame, Checkbutton, StringVar, IntVar, Radiobutton
from tkinter.ttk import Progressbar
import os
from PIL import Image, ImageTk

def open_images():
    file_paths = filedialog.askopenfilenames()
    if file_paths:
        for file_path in file_paths:
            image = Image.open(file_path)
            image.thumbnail((500, 500))
            photo = ImageTk.PhotoImage(image)
            images.append((photo, image, file_path))

        show_resize_view()

def show_resize_view():
    drop_area.pack_forget()
    resize_frame.pack(side="left", padx=20, pady=20)
    image_canvas.pack(side="left", padx=20, pady=20)
    status_label.pack(side="bottom", pady=10)
    progress_bar.pack(side="bottom", pady=10)

    for i, (photo, _, _) in enumerate(images):
        image_canvas.create_image(0, i * 100, anchor="nw", image=photo)

def resize_images():
    selected_size = size_var.get()
    selected_ratio = ratio_var.get()
    compress = compress_check_var.get()

    total_images = len(images)
    processed_images = 0

    export_dir = os.path.join(os.path.dirname(__file__), "Export")
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)

    for _, image, file_path in images:
        # Resize the image based on the selected size and ratio
        # You need to implement the actual resizing logic here
        resized_image = image.resize((500, 500))  # Placeholder code

        # Compress the image if the compress checkbox is checked
        if compress:
            # Implement image compression logic here
            # You need to replace the placeholder code below
            compressed_image = resized_image  # Placeholder code
        else:
            compressed_image = resized_image

        # Save the processed image to the export directory
        file_name = os.path.basename(file_path)
        save_path = os.path.join(export_dir, file_name)
        compressed_image.save(save_path)

        processed_images += 1
        progress = int((processed_images / total_images) * 100)
        progress_bar["value"] = progress
        root.update()

    status_label.config(text="Images processed and saved successfully!")

root = Tk()
root.title("Image Resizer")

images = []

drop_area = Label(root, text="Drop Area for Images", font=("Arial", 14))
drop_area.pack(pady=20)

open_button = Button(root, text="Open Image(s)", font=("Arial", 12), command=open_images)
open_button.pack(pady=10)

resize_frame = Frame(root)

size_label = Label(resize_frame, text="Image Size:", font=("Arial", 12))
size_label.pack()

sizes = ["Small", "Medium", "Large"]
size_var = StringVar()
size_var.set(sizes[0])

for size in sizes:
    size_radio = Radiobutton(resize_frame, text=size, font=("Arial", 12), variable=size_var, value=size)
    size_radio.pack()

ratio_label = Label(resize_frame, text="Image Ratio:", font=("Arial", 12))
ratio_label.pack(pady=(10, 0))

ratios = ["1:1", "4:3", "16:9"]
ratio_var = StringVar()
ratio_var.set(ratios[0])

for ratio in ratios:
    ratio_radio = Radiobutton(resize_frame, text=ratio, font=("Arial", 12), variable=ratio_var, value=ratio)
    ratio_radio.pack()

compress_check_var = IntVar()
compress_check = Checkbutton(resize_frame, text="Compress Image", font=("Arial", 12), variable=compress_check_var)
compress_check.pack(pady=10)

process_button = Button(resize_frame, text="Process Images", font=("Arial", 12), command=resize_images)
process_button.pack(pady=10)

image_canvas = Canvas(root, width=200, height=400)
status_label = Label(root, text="Status", font=("Arial", 12))
progress_bar = Progressbar(root, length=200, mode="determinate")

root.mainloop()
