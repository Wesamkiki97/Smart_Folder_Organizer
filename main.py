"""Scripting for organize folder"""

from config import SOURCE_FOLDER 
from planner import build_plan
from file_counter import count_files_by_category
from reporter import print_preview
from mover import preview_moves
plan = build_plan(SOURCE_FOLDER)
print(plan)

summary = count_files_by_category(plan)
print(summary)

print_preview(plan,summary)
print("-----------------------------------------")
print(f"{preview_moves(SOURCE_FOLDER,plan)}")