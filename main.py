from art import logo, congrat # art module where are all ASCII arts of my project. 
import os # operation system module which help me to clear console screen. 
 

print(logo)
# list of users and bids in auction
bids = {}
# there is a function where user name as key and bid as value would be insert in dictionary 
# and that dictionary move in auction list as list item. 
def start_auction(name, bid):
    bids[name] = bid

# function where are all records of bids and highest one will be winner after the for loop . 
def high_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"\nThe auction's Winner is {winner} with a bid of ${highest_bid}\n{congrat}")
isAuction = True
while isAuction:
    # call the function and ask user about name and bid value.
    start_auction(name = input("What is your name? : "),
    bid = float(input("Place your BID please: $")))
    # Clearing the Screen
    os.system('clear')
    # ask users if any other bids is or not . if answer is yes 
    # call again this function if not break function.
    q_a = input("Is Any other bids?(Text: Yes or No) :").lower()
    if q_a == "yes":
        isAuction = True
    else:
        isAuction = False
        high_bidder(bids)