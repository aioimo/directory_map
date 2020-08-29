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


def main():
  print("**Welcome to dirctory map")
  print("**")

  print(" ** Menu ** ")
  print("1. Select a directory")
  print("2. Quit")

  d = input()

  if d == "2":
    raise SystemExit(0)
  elif d == "1":
    root = tk.Tk()
    root.withdraw()

  print("Select your file...")
  home =  filedialog.askdirectory()
  list_files(home)






main()