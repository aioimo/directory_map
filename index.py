import os
import tkinter as tk
from tkinter import filedialog
from actions import keep_going, select_folder, get_user_input, greeting, goodbye

def list_files(rootpath):
  for root, dirs, files in os.walk(rootpath):
    level = root.replace(rootpath, "").count(os.sep)
    indent = " " * 4 * level
    print(indent + os.path.basename(root))
    subindent = " " * 4 * (level + 1)
    for file in files:
      file_path = os.path.join(root, file)
      file_size = os.path.getsize(file_path)
      print(subindent + file + "(" + str(file_size) +")")



def main():
  greeting()
  d = get_user_input()

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

      d = get_user_input()

    else:
      print("Invalid command.")
      d = get_user_input()
      
  goodbye()

main()