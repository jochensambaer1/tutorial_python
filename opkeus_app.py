import os
import shutil

def organize_desktop():
    desktop_path = 'C:\\Users\\joche\\OneDrive\\Desktop'
    files = os.listdir(desktop_path)

    for file in files:
        if os.path.isfile(os.path.join(desktop_path, file)):
            file_extension = os.path.splitext(file)[1]
            folder_path = os.path.join(desktop_path, file_extension[1:].lower() + "_files")

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            shutil.move(os.path.join(desktop_path, file), os.path.join(folder_path, file))

organize_desktop()
