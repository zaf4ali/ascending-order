import os


folder_path = "C:\Users\zafar\OneDrive\Desktop\Output"


files = os.listdir(folder_path)


files = sorted(files, key=lambda f: (os.path.join(folder_path, f)))

print(files)
