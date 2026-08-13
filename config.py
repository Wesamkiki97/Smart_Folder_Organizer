"""Configuration settings for the Smart Folder Organizer."""

from pathlib import Path


# Change this value if you want to organize a different folder.
SOURCE_FOLDER = Path.home() / "Downloads"

CATEGORIES = {
    "jpg": "Images",
    "png": "Images",
    "jpeg": "Images",
    "pdf": "Documents",
    "txt": "Documents",
    "docx": "Documents",
    "mp4": "Videos",
    "zip": "Archives",
}

UNKNOWN_CATEGORY = "Unknown"
OTHER_CATEGORY = "Others"

# True previews the plan without creating folders or moving files.
DRY_RUN = True
