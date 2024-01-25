# File Organizer Script

This Python script organizes files in your Downloads folder and Desktop into separate folders based on their types such as Images, Documents, PDFs, Screenshots, and Other.

## How to Use

1. Clone or download the repository to your local machine.

```bash
git clone https://github.com/stephen-mahon/file-organiser.git
```

2. Navigate to the project folder.

```bash
cd file-organiser
```

3. Run the script with the source folders from your Home directory as command-line arguments. For example, to organise the Desktop and Downloads folders:

```bash
python file-organiser.py Desktop Downloads
```

This command will organise files from your Desktop and Downloads folders into separate destination folders based on their types into the a Documents destination folder.

## Customisation

You can customize the script by modifying the file types and folder names in the `organise.py` file under the `move_files` function.

```python
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
```

## To Do

### Testing

- Unit tests
- Integration tests
- Edge case tests
- File type cases
- Customisation tests
- Performace tests
- Error handling tests
- Cross platform tests

### `organise.py`

- Better docstrings for `move_files` function. Change the arguments from string to paths
- Better customisation for target destination folders (Images, PDFs, Screenshots, etc)
- Regex pattern matching for destination folder to simplify loop
- Option to move subfolders

### UI

Create a nice user interface.

## Licence

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
