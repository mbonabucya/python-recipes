from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)


def find_highest_bid(bidding_record):
  winner=""
  highest_bid=0
  for bid in bidding_record:
    if highest_bid < bidding_record[bid]:
      highest_bid= bidding_record[bid]
      winner=bid
  print(f"The winner is {winner} with a bid of ${highest_bid}")
      
    
bids = {}
bidding_finished = False

while not bidding_finished:
  name = input("What is your name? ")
  price = int(input("What is your bid? $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
  elif should_continue == "yes":
    clear()
find_highest_bid(bids)
