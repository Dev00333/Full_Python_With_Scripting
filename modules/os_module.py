import os
from datetime import datetime
print(os.cpu_count())
print(os.getcwd())
print(os.listdir())
os.chdir("C:\\Users\\Devang Mishra\\OneDrive\\Desktop")
print(os.listdir())
os.mkdir("only_delete")
os.makedirs("delete1")
os.rmdir("only_delete")
os.removedirs("delete1")
print(os.getcwd())
os.chdir("C:\\Users\\Devang Mishra\\OneDrive\\Desktop\\workspace\\python_practice")
print(os.listdir())
os.mkdir("new_folder")
os.rename("new_folder", "renamed_folder")
print(os.listdir())
print(os.stat("renamed_folder"))
mod_time = os.stat("renamed_folder").st_mtime
print(datetime.fromtimestamp(mod_time))
os.rmdir("renamed_folder")
for dirpath, dirnames, filenames in os.walk("C:\\Users\\Devang Mishra\\OneDrive\\Desktop"):
    print(f"current path: {dirpath}")
    print(f"directories: {dirnames}")
    print(f"files: {filenames}")
print(os.environ.get("USERNAME"))
'test.txt'
file_path = os.environ.get("USERNAME") + "\\test.txt"
print(file_path)
# an alternative way to do the above is using os.path.join
file_path_real = os.path.join(os.path.join(os.environ.get("USERNAME"), "test01.txt"))
print(file_path_real)
print(dir(os.path))