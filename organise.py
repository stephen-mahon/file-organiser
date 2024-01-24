import os
import shutil

def move_files(source_folder, destination_folder):
    # create destination folders if they don"t already exist
    for folder in ["Images", "PDFs", "Screenshots", "Documents", "Other"]:
        folder_path = os.path.join(destination_folder, folder)
        os.makedirs(folder_path, exist_ok = True)

    # loop through all the files in the source folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # skip directories
        if os.path.isdir(file_path):
            continue

        # move file to appropriate folder
        if filename.lower().startswith("screen shot"):
            shutil.move(file_path, os.path.join(destination_folder, "Screenshots", filename))
        elif filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            shutil.move(file_path, os.path.join(destination_folder, "Images", filename))
        elif filename.lower().endswith((".doc", ".docx", ".xlsx", ".ppt", ".txt")):
            shutil.move(file_path, os.path.join(destination_folder, "Documents", filename))
        elif filename.lower().endswith(".pdf"):
            shutil.move(file_path, os.path.join(destination_folder, "PDFs", filename))
        else:
            shutil.move(file_path, os.path.join(destination_folder, "Other", filename))
