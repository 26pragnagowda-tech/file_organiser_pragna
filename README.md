Task 22 – Build a File Organizer

Project Description

The File Organizer is a Python automation project that scans a folder and automatically organizes files into different folders based on their file extensions.

For example, images are moved into an Images folder, documents into a Documents folder, and videos into a Videos folder.

Objective

To learn filesystem automation using Python and reduce manual file-management work.

Technologies Used

- Python
- pathlib
- os
- shutil

Features

1. Automatically scans a selected folder.
2. Identifies files based on their extensions.
3. Creates folders automatically.
4. Moves files into their respective folders.
5. Handles duplicate filenames safely.
6. Moves unknown file types into an Others folder.

Project Structure

File_Organizer/
│
├── file_organizer.py
├── README.md
└── Test_Folder/
    ├── image.jpg
    ├── document.pdf
    ├── video.mp4
    └── song.mp3

How to Run the Project

Step 1: Install Python on your computer.

Step 2: Open the project folder in VS Code.

Step 3: Open the terminal.

Step 4: Run the following command:

python3 file_organizer.py

Step 5: Enter the folder path when requested.

The program will automatically organize the files.

Expected Output

Before:

Test_Folder/
├── image.jpg
├── document.pdf
├── video.mp4
└── song.mp3

After:

Test_Folder/
├── Images/
│   └── image.jpg
├── Documents/
│   └── document.pdf
├── Videos/
│   └── video.mp4
└── Audio/
    └── song.mp3

Interview Questions

1. What is pathlib?

Pathlib is a Python module used to work with file and folder paths in an easy and readable way.

2. What is the difference between os and shutil?

The os module provides operating system and directory operations, while shutil provides high-level file operations such as copying and moving files.

3. How can Python automate repetitive file-management tasks?

Python can scan folders, identify file extensions, create directories, rename files and move files automatically.

Conclusion

This project demonstrates how Python can automate file-management tasks, save time and organize files efficiently.
