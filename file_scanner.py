"""Scan the Folder and return a list of files"""
from pathlib import Path

def scan_folder(folder_path:str) -> list[Path]: 
    folder = Path(folder_path)
    files=[]
    for file in folder.iterdir():
        if file.is_file():
            files.append(file)
    return files