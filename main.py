import os
import pathlib

from datetime import datetime

# Ask user for a prefix
prefix = input("Enter the prefix for renaming the images: ")

rootDir = "."
# Collect all jpg, png, and gif files
image_files = [path for path in pathlib.Path(rootDir).iterdir() 
               if path.suffix.lower() in {".jpg", ".png", ".gif"}]

# Sort files to maintain order
image_files.sort()

# Rename files sequentially with user-specified prefix
for index, path in enumerate(image_files, start=1):
    fileName, fileExtension = os.path.splitext(path.name)
    
    # Convert index to a string with leading zeros (optional, for better formatting)
    indexStr = str(index).zfill(3)  # Adjust padding as needed

    # Create the new file name
    newFileName = f"{prefix}_{fileName}_{indexStr}{path.suffix.lower()}"
    newFilePath = path.parent / newFileName
    
    # Rename the file
    os.rename(path, newFilePath)
    print(f"Renamed {path} to {newFilePath}")

