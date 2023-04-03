import os


folder_path = "output"


files = os.listdir(folder_path)


files = sorted(files, key=lambda f: (os.path.join(folder_path, f)), reverse=True)

print(files)
