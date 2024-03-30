import random
from art import logo
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def compare(guess, number):
  """ take guess , computer generated and attemts and return the number of attempts left and whether lost or won"""
  
  if guess > number:
    return "Too high."
  elif guess < number:
    return "Too low."
  else:
    return "You got it!"

def play():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  computer_number = random.randint(1,100)
  if difficulty == "easy":
    attempts = 10
  else:
    attempts = 5

    

  while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_number = int(input("Guess a number between 1 and 100: "))
   
    print(f"computer number {computer_number}")
    guess = compare(guess=user_number, number=computer_number)
    if guess == "You got it!":
      print(f"You got it! The answer was {computer_number}.")
      attempts = 0
    else:
      print(guess)
      attempts -= 1
      if attempts > 0:
        print("Guess again.")
      else:
        print("You've run out of guesses, you lose.")
  
play()



  



