"""Scripting for organize folder"""

from config import SOURCE_FOLDER ,DRY_RUN
from planner import build_plan
from file_counter import count_files_by_category
from reporter import print_full_preview
from mover import create_category_folders, preview_moves , move_files



plan = build_plan(SOURCE_FOLDER)
summary = count_files_by_category(plan)
folder_summary = create_category_folders(SOURCE_FOLDER , plan)
moves_preview = preview_moves(SOURCE_FOLDER,plan)



if DRY_RUN :
    print_full_preview(
        plan,
        summary,
        folder_summary,
        moves_preview
        )
else:
    move_summary = move_files(SOURCE_FOLDER,plan)
    print(move_summary)

# print(moves_preview)