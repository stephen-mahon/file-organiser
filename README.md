# File Organizer Script

This Python script organizes files in your Downloads folder and Desktop into separate folders based on their types, such as Images, Documents, PDFs, Screenshots, and Other.

## How to Use

1. Clone or download the repository to your local machine.

```bash
git clone https://github.com/stephen-mahon/file-organiser.git
```

2. Navigate to the project folder.

```bash
cd file-organiser
```

3. Edit the script (organizer.py) to set the correct paths for your Downloads folder, Desktop, and the destination folder where you want to organize the files.

```python
downloads_folder = Path.home() / 'Downloads'
desktop_folder = Path.home() / 'Desktop'
destination_folder = Path.home() / 'Documents'
```

4. Run the script.

```bash
python main.py
```

The script will organize files from the Downloads folder and Desktop into the specified destination folder.

## Customisation

You can customize the script by modifying the file types and folder names in the `organise.py` file under the `move_files` function.

```python
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
```

## To Do

### Testing
- Unit tests
- Integration tests
- Edge case tests
- File type cases
- Customisation tests
- Performance tests
- Error handling tests
- Cross-platform tests

### UI
Create a nice user interface.


## Licence

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
