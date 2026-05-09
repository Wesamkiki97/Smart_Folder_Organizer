"""Generator "Report" to show the files in the folder"""
def print_preview(plan,summary):
    print(f"""Smart Folder Organizer Preview\n""")
    for category, files in plan.items():
        print(f"{category} ({len(files)} files):")
        for file in files:
            print(f"- {file.name}")
        print()
    print(f"Summary:")
    for category, file_num in summary.items():
        print(f"{category}: {file_num}")


def print_full_preview(plan,summary,folder_summary,moves_preview):
    print(f"""Smart Folder Organizer Preview\n""")
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
    print("folder execution:")
    for status, folders in folder_summary.items():
        print(f"{status}:")
        for folder in folders:
            print(f"-{folder}")
        print()
    print("---------------------------------")
    print("moves files summary:")
    for transaction in moves_preview:
        print(".......................")
        for key, value in transaction.items():
            print(f"{key}: {value}")
