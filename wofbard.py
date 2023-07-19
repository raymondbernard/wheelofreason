import random

def spin_wheel():
  """Returns a random number between 0 and 51."""
  return random.randint(0, 51)

def call_letter(letter, puzzle):
  """Returns True if the letter is in the puzzle, False otherwise."""
  if letter in puzzle:
    return True
  else:
    return False

def buy_vowel(vowel, puzzle):
  """Returns True if the vowel is in the puzzle, False otherwise."""
  if vowel in puzzle:
    return True
  else:
    return False

def solve_puzzle(puzzle):
  """Returns the solution to the puzzle."""
  words = puzzle.split(" ")
  solution = ""
  for word in words:
    solution += word
  return solution

def main():
  """Plays a game of Wheel of Fortune."""
  puzzle = "ACROSS THE RIVER"
  llms = []
  for i in range(3):
    llm = Bard()
    llms.append(llm)
  human = input("Enter your name: ")

  for i in range(4):
    turn = random.randint(0, 3)
    if turn == 3:
      print("It's your turn, {}!".format(human))
    else:
      print("It's LLM {}'s turn!".format(turn))
    spin = spin_wheel()
    if spin == 0:
      print("Bankrupt!")
    elif spin == 250:
      vowel = input("Buy a vowel? (Y/N): ")
      if vowel == "Y":
        vowel = input("Which vowel? ")
        if buy_vowel(vowel, puzzle):
          print("You got it!")
        else:
          print("Sorry, that's not in the puzzle.")
      else:
        print("Pass.")
    else:
      letter = input("Call a letter: ")
      if call_letter(letter, puzzle):
        print("You got it!")
      else:
        print("Sorry, that's not in the puzzle.")

  solution = solve_puzzle(puzzle)
  print("The solution is: {}".format(solution))

if __name__ == "__main__":
  main()
