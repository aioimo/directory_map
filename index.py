import os
import tkinter as tk
from tkinter import filedialog

from actions import keep_going, select_folder, get_user_input, greeting, goodbye


ONE_kB = 2**10
ONE_MB = 2**20


def bytes_to_kb(number_bytes):
  return round(number_bytes/ONE_kB)


def bytes_to_mb(number_bytes):
  return round(number_bytes/2**20, 2)


def format_bytes(number_bytes):
  if number_bytes < 2**20:
    return str(bytes_to_kb(number_bytes)) + " kB"
  return str(bytes_to_mb(number_bytes)) + " MB"


def list_files(rootpath):
  for root, dirs, files in os.walk(rootpath):
    level = root.replace(rootpath, "").count(os.sep)
    indent = " " * 4 * level
    print(indent + os.path.basename(root))
    subindent = " " * 4 * (level + 1)
    for file in files:
      file_path = os.path.join(root, file)
      number_bytes = os.path.getsize(file_path)
      print(subindent + file + " (" + format_bytes(number_bytes) +")")


def main():
  greeting()
  action = get_user_input()

  pristine = True

  while keep_going(action):
    if select_folder(action):
      print("Select directory when prompted...")
      if pristine:
        root = tk.Tk()
        root.withdraw()
        pristine = False

      root =  filedialog.askdirectory()
      list_files(root)

      action = get_user_input()

    else:
      print("Invalid command.")
      action = get_user_input()
      
  goodbye()

main()