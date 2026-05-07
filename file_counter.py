"""Ewcive list of files and return summery of files counter"""
def count_files_by_category(plan):
   files_num = {}
   for key,value in plan.items():
        files_num[key] = len(value)
   return files_num

