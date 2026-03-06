# Smart File Organizer
# Author: Satyam Gupta
# Python automation project

import os
import shutil

folder_path = input("Enter folder path to organize: ")

file_types = {
    "Images": [".jpg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4"],
    "Archives": [".zip", ".rar"]
}

files = os.listdir(folder_path)

for file in files:
    path = os.path.join(folder_path, file)

    if os.path.isfile(path):
        ext = os.path.splitext(file)[1].lower()

        for folder, extensions in file_types.items():
            if ext in extensions:

                new_folder = os.path.join(folder_path, folder)

                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)

                shutil.move(path, os.path.join(new_folder, file))
                break

print("Files organized successfully!")