
SELECT = "select"
QUIT = "quit"


input_to_actions = {
  "1": SELECT,
  "quit": QUIT,
  "q": QUIT,
  "2": QUIT
}

def actions(d):
  if d in input_to_actions:
    return input_to_actions[d]

def keep_going(decision):
  return actions(decision) != QUIT

def select_folder(decision):
  return actions(decision) == SELECT

def menu():
  print("**")
  print("1. Select a directory")
  print("2. Quit")
  return input()

