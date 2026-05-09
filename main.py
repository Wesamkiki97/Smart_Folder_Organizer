"""Scripting for organize folder"""

from config import SOURCE_FOLDER 
from planner import build_plan
from file_counter import count_files_by_category
from reporter import print_full_preview
from mover import create_category_folders, preview_moves 



plan = build_plan(SOURCE_FOLDER)
summary = count_files_by_category(plan)
folder_summary = create_category_folders(SOURCE_FOLDER , plan)
moves_preview = preview_moves(SOURCE_FOLDER,plan)




print_full_preview(
    plan,
    summary,
    folder_summary,
    moves_preview
    )
# print(moves_preview)