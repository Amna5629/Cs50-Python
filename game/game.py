import random

def get_positive_integer(prompt):

  while True:
    try:
      value = int(input(prompt))
      if value > 0:
        return value
      else:
        print("Please enter a positive integer.")
    except ValueError:
      print("Invalid input. Please enter a positive integer.")

def main():

  level = get_positive_integer("Enter the level (positive integer): ")


  number = random.randint(1, level)

  guess = 0
  while guess != number:
    try:
      guess = int(input("Guess a number between 1 and {}: ".format(level)))
      if guess < 1:
        print("Guess must be a positive integer.")
      elif guess < number:
        print("Too small!")
      elif guess > number:
        print("Too large!")
    except ValueError:
      print("Invalid input. Please enter an integer.")

  # User guessed correctly
  print("Just right!")

if __name__ == "__main__":
  main()
