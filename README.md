# Image Resizing & Compression

This is a Python-based desktop application that allows you to resize and compress images. It provides a user-friendly interface for selecting images, specifying the desired dimensions and compression, and processing the images accordingly.

## Features

- Drag and drop multiple images for resizing and compression.
- Choose the desired dimensions (width and height) for the images.
- Select a ratio to maintain the aspect ratio of the images.
- Option to compress the images automatically.
- Progress bar to track the processing status.
- Preview of the processed images.
- Exported images stored in an "Export" folder next to the script.

- Requirements

- Python 3.x
- Pillow library: Install using `pip install Pillow`

- Usage

1. Clone the repository or download the project files.

2. Install the required dependencies by running the following command:

# pip install Pillow

3. Run the script `image_resizer.py` using Python:

# python image_resizer.py

4. The application window will appear, allowing you to drag and drop images, select dimensions and ratio, and enable image compression. Click the "Process Images" button to start the resizing and compression process.

5. Processed images will be saved in an "Export" folder located next to the script.

- Creating an Executable

You can convert the script into an executable file using PyInstaller to run the application without requiring Python to be installed. Follow these steps to create an executable:

1. Install PyInstaller:

# pip install pyinstaller

2. Navigate to the project directory in the command prompt.

3. Convert the script into an executable:

# pyinstaller --onefile image_resizer.py

This will create an executable file in the `dist` directory.

4. Locate the generated executable file (`image_resizer.exe`) in the `dist` directory and run it.

- Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

- License

This project is licensed under the [MIT License](LICENSE).
