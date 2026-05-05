"""Classify the file's extension and return the category"""
from pathlib import Path
from config import CATEGORIES, UNKNOWN_CATEGORY, OTHER_CATEGORY
def classify_file(file_path: str) -> str:
    file = Path(file_path)
    if not file.suffix:
        return UNKNOWN_CATEGORY
    extension = file.suffix[1:].lower()
    return CATEGORIES.get(extension,OTHER_CATEGORY)