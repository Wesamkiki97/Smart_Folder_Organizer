"""Scripting for organize folder"""

from config import SOURCE_FOLDER 
from planner import build_plan
from file_counter import count_files_by_category

plan = build_plan(SOURCE_FOLDER)
print(plan)

summary = count_files_by_category(plan)
print(summary)