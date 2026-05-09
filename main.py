"""Scripting for organize folder"""

from config import SOURCE_FOLDER 
from planner import build_plan
from file_counter import count_files_by_category
from reporter import print_preview
from mover import create_category_folders, preview_moves 



plan = build_plan(SOURCE_FOLDER)
summary = count_files_by_category(plan)
folder_summary = create_category_folders(SOURCE_FOLDER , plan)
moves_preview = preview_moves(SOURCE_FOLDER,plan)


print_preview(plan,summary)
print("-----------------------------------------")
print(folder_summary)
print("-----------------------------------------")
print(moves_preview)