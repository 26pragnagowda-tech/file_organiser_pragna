import os
import shutil
from pathlib import Path

# File categories and extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Archives": [".zip", ".rar"],
    "Code": [".py", ".html", ".css", ".js"]
}


def organize_files(folder_path):

    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        print("Invalid folder path!")
        return

    for file in folder.iterdir():

        if file.is_file():
            extension = file.suffix.lower()

            category = "Others"

            for folder_name, extensions in FILE_TYPES.items():
                if extension in extensions:
                    category = folder_name
                    break

            destination_folder = folder / category
            destination_folder.mkdir(exist_ok=True)

            destination = destination_folder / file.name

            # Handle duplicate filenames
            counter = 1
            while destination.exists():
                destination = destination_folder / (
                    f"{file.stem}_{counter}{file.suffix}"
                )
                counter += 1

            shutil.move(str(file), str(destination))

            print(f"Moved {file.name} to {category}")


if __name__ == "__main__":

    path = input("Enter folder path to organize: ")

    organize_files(path)

    print("File organization completed!")
