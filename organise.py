import logging
import os
import shutil

def move_files(source_folder, destination_folder):
    # create destination folders if they don't already exist
    for folder in ["Images", "PDFs", "Screenshots", "Documents", "Other"]:
        folder_path = os.path.join(destination_folder, folder)
        os.makedirs(folder_path, exist_ok = True)

    # loop through all the files in the source folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # skip directories
        if os.path.isdir(file_path):
            continue

        # define the destination folder
        if filename.lower().startswith("screen shot"):
            destination= os.path.join(destination_folder, "Screenshots", filename)
        elif filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            destination = os.path.join(destination_folder, "Images", filename)
        elif filename.lower().endswith((".doc", ".docx", ".xlsx", ".ppt", ".txt")):
            destination = os.path.join(destination_folder, "Documents", filename)
        elif filename.lower().endswith(".pdf"):
            destination = os.path.join(destination_folder, "PDFs", filename)
        else:
            destination = os.path.join(destination_folder, "Other", filename)

        # log the file move
        log(f"moving {file_path} to {destination}")

        # move file to appropriate folder
        shutil.move(file_path, destination)


# basic logger for tracking file changes
def log(message):
    # set the date format to 2024/01/25 10:34:36 AM
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p')
    logging.warning(message)