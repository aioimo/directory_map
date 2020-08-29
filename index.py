import os
import tkinter as tk
from tkinter import filedialog
from actions import keep_going, select_folder, menu

def list_files(rootpath):
  for root, dirs, files in os.walk(rootpath):
    level = root.replace(rootpath, "").count(os.sep)
    indent = " " * 4 * level
    print(indent + os.path.basename(root))
    subindent = " " * 4 * (level + 1)
    for file in files:
      print(subindent + file)


def greeting():
  print("**Welcome to dirctory map")

def goodbye():
  print("Goodbye.")

def main():
  greeting()
  d = menu()

  pristine = True

  while keep_going(d):
    if select_folder(d):
      print("Select directory when prompted...")
      if pristine:
        root = tk.Tk()
        root.withdraw()
        pristine = False

      root =  filedialog.askdirectory()
      list_files(root)

      d = menu()

    else:
      print("Invalid command.")
      d = menu()
      
  goodbye()

main()