import os
import tkinter as tk
from tkinter import filedialog

def list_files(rootpath):
  for root, dirs, files in os.walk(rootpath):
    level = root.replace(rootpath, "").count(os.sep)
    indent = " " * 4 * level
    print(indent + os.path.basename(root))
    subindent = " " * 4 * (level + 1)
    for file in files:
      print(subindent + file)





print("Welcome to dirctory map\n")
d = input("Press y to select a directory, press n to quit: ")

if d == "n":
  raise SystemExit(0)
elif d == "y":
  root = tk.Tk()
  root.withdraw()



# home = print("Please enter the root directory: ")

print("Select your file...")
home =  filedialog.askdirectory()






list_files(home)