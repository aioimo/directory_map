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


def greeting():
  print("**Welcome to dirctory map")

def goodbye():
  print("Goodbye.")


def menu():
  print("**")
  print("1. Select a directory")
  print("2. Quit")
  return input()

def end_script():
  raise SystemExit(0)

def keep_going(decision):
  return decision != "2" and decision != "quit" and decision != "q"


def main():
  greeting()
  d = menu()

  pristine = True

  while keep_going(d):
    if d == "1":
      if pristine:
        root = tk.Tk()
        root.withdraw()
        pristine = False

      print("Select directory when prompted...")
      home =  filedialog.askdirectory()
      list_files(home)

      d = menu()
    else:
      print("Invalid command")
      d = menu()
      
  goodbye()


main()