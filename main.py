"""Scripting for organize folder"""
from config import SOURCE_FOLDER 
from file_scanner import scan_folder
from classifier import classify_file
#from CATEGORIES
#     "Images" ,
#     "Documents" ,
#     "Videos" ,
#     "Archives",
#     "Others" 
# 

def build_plan(folder):
    files = scan_folder(folder)
    building={}
    for file in files:
        category = classify_file(file)
        if category in building:
         building[category].append(file.name)
        else:
         building[category] = [file.name]
    return building

plan = build_plan(SOURCE_FOLDER)
print(plan)


def count_files_by_category(files_structure):
   files_num = {}
   for key,value in files_structure.items():
        files_num[key] = len(value)
   return files_num

summary = count_files_by_category(plan)
print(summary)