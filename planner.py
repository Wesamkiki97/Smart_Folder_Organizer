"""Build Plan"""
from classifier import classify_file
from file_scanner import scan_folder 
def build_plan(folder):
    files = scan_folder(folder)
    plan={}
    for file in files:
        category = classify_file(file)
        if category in plan:
         plan[category].append(file.name)
        else:
         plan[category] = [file.name]
    return plan

