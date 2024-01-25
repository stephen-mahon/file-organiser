# File Organizer Script

This Python script organizes files in your Home directory folders into separate folders in Documents based on their types, such as Images for `.png`, `.jpg`, `.jpeg`, `.gif`, Documents for `.doc`, `.docx`, `.xlsx`, `.ppt`, `.txt`, PDFs for `.pdf`, Screenshots, and Other.

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

Files from your Desktop and Downloads folders will be organised into separate destination folders in Documents based on their types.

## Customisation

You can customize the script by modifying the file types and folder names in the `organise.py` file under the `move_files` function.

```python
pattern_destination = {
    r"^screen\s?shot": "Screenshots",
    r"\.(png|jpg|jpeg|gif)$": "Images",
    r"\.pdf$": "PDFs",
    r"\.(doc.?|xls.?|ppt.?|txt)": "Documents",
}
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

### `organise.py`

- Better docstrings for `move_files` function. Change the arguments from string to paths
- Better customisation for target destination folders (Images, PDFs, Screenshots, etc)
- Regex pattern matching for destination folder to simplify loop
- Option to move subfolders

### UI

Create a nice user interface.

## Licence

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
