"""Create category folders and move files into them."""

import shutil
from pathlib import Path


def create_category_folders(source_path, plan):
    source = Path(source_path)
    summary = {
        "created": [],
        "already_exists": [],
        "failed": [],
    }
    for category in plan:
        folder_path = source / category
        if folder_path.exists():
            summary["already_exists"].append(category)
        else:
            try:
                folder_path.mkdir(parents=True)
                summary["created"].append(category)
            except PermissionError:
                message = "You do not have permission to create folders here."
                summary["failed"].append({"category": category, "error": message})
            except OSError as error:
                message = f"The path is invalid or there is a system issue: {error}"
                summary["failed"].append({"category": category, "error": message})

    return summary


def preview_moves(source_path, plan):
    source = Path(source_path)
    summary = []
    for category, files in plan.items():
        for file in files:
            file_destination = source / category / file.name
            if file_destination.exists():
                summary.append({
                    "file": file.name,
                    "from": str(file),
                    "to": str(file_destination),
                    "status": "skipped_duplicate",
                })
                continue
            summary.append({
                "file": file.name,
                "from": str(file),
                "to": str(file_destination),
                "status": "ready",
            })
    return summary


def move_files(source_path, plan):
    source = Path(source_path)
    summary = []

    for category, files in plan.items():
        for file in files:
            folder_destination = source / category
            file_destination = source / category / file.name

            if not folder_destination.exists():
                summary.append({
                    "file": file.name,
                    "from": str(file),
                    "to": str(file_destination),
                    "status": "failed",
                    "message": "The destination folder does not exist.",
                })
                continue

            if file_destination.exists():
                summary.append({
                    "file": file.name,
                    "from": str(file),
                    "to": str(file_destination),
                    "status": "skipped_duplicate",
                    "message": "A file with the same name already exists.",
                })
                continue
            try:
                shutil.move(str(file), str(file_destination))
                summary.append({
                    "file": file.name,
                    "from": str(file),
                    "to": str(file_destination),
                    "status": "moved",
                    "message": "The file was moved.",
                })
            except FileNotFoundError:
                summary.append({
                    "file": file.name,
                    "from": str(file),
                    "to": str(file_destination),
                    "status": "failed",
                    "message": "The source file was not found.",
                })
            except OSError as error:
                summary.append({
                    "file": file.name,
                    "from": str(file),
                    "to": str(file_destination),
                    "status": "failed",
                    "message": f"System error: {error}",
                })
    return summary
