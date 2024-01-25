import logging
import os
import re
import shutil

def move_files(source_folder, destination):
    # create destination folders if they don't already exist
    for folder in ["Images", "PDFs", "Screenshots", "Documents", "Other"]:
        folder_path = os.path.join(destination, folder)
        os.makedirs(folder_path, exist_ok = True)

    # define the file patterns and their corresponding destination dictionary
    pattern_destination = {
        r"^screen\s?shot": "Screenshots",
        r"\.(png|jpg|jpeg|gif)$": "Images",
        r"\.pdf$": "PDFs",
        r"\.(doc.?|xls.?|ppt.?|txt)": "Documents",
    }


    # loop through all the files in the source folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # skip directories
        if os.path.isdir(file_path):
            continue

        matched = False

        # determine the file type using the regex pattern
        for pattern, destination_folder in pattern_destination.items():
            if re.search(pattern, filename, re.IGNORECASE):
                destination_path = os.path.join(destination, destination_folder, filename)
                # log the file move
                log(f"moving {file_path} to {destination_path}")
                shutil.move(file_path, destination_path)
                matched = True
                break
        
        if not matched:
            destination_path = os.path.join(destination, destination_folder, filename)
            log(f"moving {file_path} to {destination_path}")
            shutil.move(file_path, destination_path)


# basic logger for tracking file changes
def log(message):
    # set the date format to 2024/01/25 10:34:36 AM
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p')
    logging.warning(message)