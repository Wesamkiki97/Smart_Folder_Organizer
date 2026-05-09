"""Create folders and move the files """
from pathlib import Path
import shutil

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
        for file in files:
            file_destination = source / category / file.name
            if file_destination.exists():
                summary.append({
                    "file" : file.name,
                    "from" : str(file),
                    "to"   : str(file_destination),
                    "status" : "skipped_duplicate"
                    })
                continue
            summary.append({
                "file" : file.name,
                "from" : str(file),
                "to"   : str(file_destination),
                "status" : "ready"
                })
    return summary

def move_files(source_path,plan):
    source = Path(source_path)
    summary =[]

    for category, files in plan.items():
        for file in files:
            folder_destination = source / category
            file_destination = source / category / file.name
           
            if not folder_destination.exists():
                summary.append({
                       "file" : file.name,
                       "from" : str(file),
                       "to"   : str(file_destination),
                       "status" :"failed",
                       "message" : "the destination folder is incorrect"
                       })
                continue
           
            if file_destination.exists():
                summary.append({
                        "file" : file.name,
                        "from" : str(file),
                        "to"   : str(file_destination),
                        "status" :"skipped_duplicate",
                        "message" : "there is a file in same name"
                        })
                continue
            try:   
                shutil.move(str(file),str(file_destination)) 
                summary.append({
                    "file" : file.name,
                    "from" : str(file),
                    "to"   : str(file_destination),
                    "status" : "moved",
                    "message" : "The file has moved"
                    })
            except FileNotFoundError:
                summary.append({
                    "file" : file.name,
                    "from" : str(file),
                    "to"   : str(file_destination),
                    "status" :"failed",
                    "message" : "the destination file is incorrect"
                    })
            except OSError as e:
                 summary.append({
                    "file" : file.name,
                    "from" : str(file),
                    "to"   : str(file_destination),
                    "status" :"failed",
                    "message" : f"system error: {e}"
                    })
    return summary