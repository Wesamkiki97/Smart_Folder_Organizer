"""Scan the Folder and list the file then send it one by one to classifier and resort it """
from pathlib import Path
from classifier import classify_file

tempDB = {}
def scanner(folder_path:str): 
    folder = Path(folder_path)
    for file in folder.iterdir():
        
        tempDB[file.name] = classify_file(Path(file))