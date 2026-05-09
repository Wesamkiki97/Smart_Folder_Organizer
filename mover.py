"""Create folders and move the files """
from pathlib import Path
def create_category_folders(source_path,plan):
    source = Path(source_path)
    summary ={
         "created" : [],
         "already_exists" : [],
         "failed" : []
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
                message = f"Error You don't have permission to create folders here."
                summary["failed"].append({"category": category,"error": message})

            except OSError as e:
                message= f"Error: The path is invalid or there is a system issue: {e}"
                summary["failed"].append({"category": category,"error": message})
                             
    return summary
def preview_moves(source_path, plan):
    source = Path(source_path)
    summary =[]
    for category, files in plan.items():
        folder_path = source / category
        for file in files:
            file_path = folder_path / file.name
            summary.append({
                "file" : f"{file.name}",
                "from" : str(file),
                "to"   : str(file_path)
                })
    return summary