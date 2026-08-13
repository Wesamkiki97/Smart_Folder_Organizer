"""Scan a folder and return its files."""

from pathlib import Path

def scan_folder(folder_path: str | Path) -> list[Path]:
    folder = Path(folder_path)
    files = []
    for file in folder.iterdir():
        if file.is_file():  # Check whether the path points to a file.
            files.append(file)
    return files