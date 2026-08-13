"""Print readable previews and execution results."""


def print_preview(plan, summary):
    print("Smart Folder Organizer Preview\n")
    for category, files in plan.items():
        print(f"{category} ({len(files)} files):")
        for file in files:
            print(f"- {file.name}")
        print()
    print("Summary:")
    for category, file_num in summary.items():
        print(f"{category}: {file_num}")


def print_full_preview(plan, summary, folder_summary, moves_preview):
    print("Smart Folder Organizer Preview\n")
    print("Scan source folder preview:")
    for category, files in plan.items():
        print(f"{category} ({len(files)} files):")
        for file in files:
            print(f"- {file.name}")
        print()
    print("---------------------------------")
    print("Summary of files:")
    for category, file_num in summary.items():
        print(f"{category}: {file_num}")
    print("---------------------------------")
    print("Folder execution:")
    for status, folders in folder_summary.items():
        print(f"{status}:")
        for folder in folders:
            print(f"- {folder}")
        print()
    print("---------------------------------")
    print("File move preview:")
    for transaction in moves_preview:
        print(".......................")
        for key, value in transaction.items():
            print(f"{key}: {value}")


def print_move_summary(move_summary):
    print("\nMove result:")
    for transaction in move_summary:
        print(
            f"- {transaction['file']}: "
            f"{transaction['status']}"
        )
