import os

print("Welcome to the app\n")

# sample = "/Users/anthony/Desktop/Tuscany"

home = input("Please enter the root directory: ")



def list_files(rootpath):
  for root, dirs, files in os.walk(rootpath):
    level = root.replace(rootpath, "").count(os.sep)
    indent = " " * 4 * level
    print(indent + os.path.basename(root))
    subindent = " " * 4 * (level + 1)
    for file in files:
      print(subindent + file)



list_files(home)