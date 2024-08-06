# Image renamer in Python
# Overview

This project is a Python script designed to help users rename image files in a specified directory. The script collects image files with specified extensions (JPG, PNG, GIF), sorts them, and renames them sequentially with a user-specified prefix. The renamed files are then saved in the same directory. Notifications are provided upon successful renaming of each file.

## Features

- Collect image files with extensions .jpg, .png, and .gif from the specified directory.
- Sort the image files to maintain order.
- Rename files sequentially with a user-specified prefix.
- Provide Prints of successful renaming for each file in the terminal.

## Libraries Used

- `os`: For interacting with the operating system and handling file paths.
- `pathlib`: For handling file paths and directories.
- `datetime`: For managing date and time, if needed for future extensions.

## Prerequisites

Ensure you have Python installed. This script is compatible with Python 3

## Usage

1. Clone the repository or download the script file to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script using the following command:

    ```bash
    python your_script_name.py
    ```

4. Follow the prompts:

    - Enter the prefix for renaming the images.
    
    The script will process the image files in the current directory, rename them with the specified prefix, and provide notifications upon successful renaming of each file.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests. Your contributions are welcome!
