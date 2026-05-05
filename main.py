"""Scripting for organize folder"""
from config import SOURCE_FOLDER 
from file_scanner import scan_folder
from classifier import classify_file
from planner import build_plan
#from CATEGORIES
#     "Images" ,
#     "Documents" ,
#     "Videos" ,
#     "Archives",
#     "Others" 
#
plan = build_plan(SOURCE_FOLDER)
print( plan)



def count_files_by_category(files_structure):
   files_num = {}
   for key,value in files_structure.items():
        files_num[key] = len(value)
   return files_num

summary = count_files_by_category(plan)
print(summary)