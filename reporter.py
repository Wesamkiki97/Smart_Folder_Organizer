"""Generator "Report" to show the files in the folder"""
def print_preview(plan,summary):
    print(f"""Smart Folder Organizer Preview\n""")
    for category, files in plan.items():
        print(f"{category} ({len(files)} files):")
        for file in files:
            print(f"- {file}")
        print()
    print(f"Summary:")
    for category, file_num in summary.items():
        print(f"{category}: {file_num}")
