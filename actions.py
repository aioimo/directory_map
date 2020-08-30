
SELECT = "select"
QUIT = "quit"


input_to_actions = {
  "1": SELECT,
  "2": QUIT,
  "quit": QUIT,
  "q": QUIT,
  "Q": QUIT,
  "exit": QUIT
}

def actions(d):
  if d in input_to_actions:
    return input_to_actions[d]


def keep_going(decision):
  return actions(decision) != QUIT


def select_folder(decision):
  return actions(decision) == SELECT


def get_user_input():
  print("**")
  print("1. Select a directory")
  print("2. Quit")
  return input()


def greeting():
  print("**Welcome to dirctory map")


def goodbye():
  print("Goodbye.")
