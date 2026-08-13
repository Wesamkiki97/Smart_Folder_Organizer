# Smart Folder Organizer

A small Python script that organizes files into folders based on their extensions.
I built it to practice working with files, folders, modules, and `pathlib` while solving a simple problem in my Downloads folder.

## What it does

- Scans the selected folder.
- Classifies files by extension.
- Creates category folders such as `Images`, `Documents`, and `Videos`.
- Moves files into the matching folders.
- Skips a file when another file with the same name already exists.
- Supports a dry-run mode to preview the plan before moving anything.

## Project structure

```text
Smart_Folder_Organizer/
|-- main.py
|-- config.py
|-- file_scanner.py
|-- classifier.py
|-- planner.py
|-- file_counter.py
|-- mover.py
`-- reporter.py
```

## How to use

1. Make sure Python 3.10 or newer is installed.
2. Open `config.py` and check the folder path:

```python
SOURCE_FOLDER = Path.home() / "Downloads"
```

3. Keep `DRY_RUN = True` for the first run.
4. Run the script:

```bash
python main.py
```

5. Review the preview. When you are ready to move the files, change the setting to:

```python
DRY_RUN = False
```

Then run the script again.

## File categories

The default categories are configured in `config.py`. You can add more extensions to the `CATEGORIES` dictionary.

## Notes

- The script scans only the files directly inside the selected folder.
- It does not delete or overwrite duplicate files.
- This is a learning project and a personal automation script.
