from tkinter import Tk, Button, Label, filedialog, Canvas, Frame, Checkbutton, StringVar, IntVar
from PIL import Image, ImageTk

def open_images():
    file_paths = filedialog.askopenfilenames()
    if file_paths:
        for file_path in file_paths:
            image = Image.open(file_path)
            image.thumbnail((500, 500))
            photo = ImageTk.PhotoImage(image)
            images.append(photo)

        show_resize_view()

def show_resize_view():
    drop_area.pack_forget()
    resize_frame.pack(side="left", padx=20, pady=20)
    image_canvas.pack(side="left", padx=20, pady=20)
    status_label.pack(side="bottom", pady=10)

    for i, image in enumerate(images):
        image_canvas.create_image(0, i * 100, anchor="nw", image=image)

def resize_images():
    # Implement image resizing logic here
    pass

def compress_images():
    # Implement image compression logic here
    pass

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

# Sample size options, you can modify as needed
sizes = ["Small", "Medium", "Large"]
size_var = StringVar()
size_var.set(sizes[0])

for size in sizes:
    size_radio = Radiobutton(resize_frame, text=size, font=("Arial", 12), variable=size_var, value=size)
    size_radio.pack()

ratio_label = Label(resize_frame, text="Image Ratio:", font=("Arial", 12))
ratio_label.pack(pady=(10, 0))

# Sample ratio options, you can modify as needed
ratios = ["1:1", "4:3", "16:9"]
ratio_var = StringVar()
ratio_var.set(ratios[0])

for ratio in ratios:
    ratio_radio = Radiobutton(resize_frame, text=ratio, font=("Arial", 12), variable=ratio_var, value=ratio)
    ratio_radio.pack()

compress_check = Checkbutton(resize_frame, text="Compress Image", font=("Arial", 12))
compress_check.pack(pady=10)

process_button = Button(resize_frame, text="Process Images", font=("Arial", 12), command=resize_images)
process_button.pack(pady=10)

image_canvas = Canvas(root, width=200, height=400)
status_label = Label(root, text="Status", font=("Arial", 12))

root.mainloop()
