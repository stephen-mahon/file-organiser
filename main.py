from organise import move_files
from pathlib import Path

def main():
    # Set path to Desktop and Downloads folder
    download_folder = Path.home() / "Downloads"
    desktop_folder = Path.home() / "Desktop"

    # Set path for organised files
    destination_folder = Path.home() / "Documents"

    # Organise files from the Desktop
    move_files(desktop_folder, destination_folder)

    # Organise files from Downloads
    move_files(download_folder, destination_folder)

    print("Files organized successfully.")


if __name__ == ("__main__"):
    main()