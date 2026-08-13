"""Run the Smart Folder Organizer."""

from config import DRY_RUN, SOURCE_FOLDER
from file_counter import count_files_by_category
from mover import create_category_folders, move_files, preview_moves
from planner import build_plan
from reporter import print_full_preview, print_move_summary, print_preview


def main():
    plan = build_plan(SOURCE_FOLDER)
    summary = count_files_by_category(plan)
    moves_preview = preview_moves(SOURCE_FOLDER, plan)

    if DRY_RUN:
        print_preview(plan, summary)
        print("\nNo folders or files were changed because DRY_RUN is enabled.")
        return

    folder_summary = create_category_folders(SOURCE_FOLDER, plan)
    print_full_preview(plan, summary, folder_summary, moves_preview)
    move_summary = move_files(SOURCE_FOLDER, plan)
    print_move_summary(move_summary)

if __name__ == "__main__":
    main()