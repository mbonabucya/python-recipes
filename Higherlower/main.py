from art import logo ,vs
from game_data import data
import random

def get_random_account():
  return random.choice(data)


def extract(account):
   print(f"{account['name']} {account['description']} from {account['country']}")
  

def play():
  print(logo)
  print("Welcome to the Higher Lower Game \n")
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()
  
  while game_should_continue: 
    account_a = account_b
    account_b = get_random_account()
    extract(account_a)
    print(vs)
    extract(account_b)
    answer = input("Who has more followers? Type 'A' or 'B': ")
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
  
    if answer == "A":
      if a_follower_count > b_follower_count:
        score += 1
        print(f"You're right! Current score: {score}.")
      else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
    elif answer == "B":
      if b_follower_count > a_follower_count:
        score += 1
        account_a = account_b
        print(f"You're right! Current score: {score}.")
      else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False

play()