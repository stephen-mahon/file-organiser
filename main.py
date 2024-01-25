import sys
from organise import move_files, log
from pathlib import Path

def main():
    # Take input for source folder from command-line interface
    if len(sys.argv) == 0:
        # Quit program with error
        sys.exit("too few arguments")
    
    source_folders = []
    
    # Set path for source folders
    for folder in sys.argv[1:]:
        source_path = Path.home() / folder
        # Check if the path exists
        if source_path.exists():
            source_folders.append(source_path)
        else:
            log(f"{folder} does not exist")
    
    # Quit program with error if there are no source folders
    if len(source_folders) == 0:
        sys.exit("no folders selected")

    # Set path for organised files
    destination_folder = Path.home() / "Documents"

    # Organise files from source folders
    for path in source_folders:
        move_files(path, destination_folder)

    log("Files organisation complete.")


if __name__ == ("__main__"):
    main()