import art
print(art.logo)
print("welcome to the secret auction program.")

table_of_bids = {}
def auction():
    name = input("what is your name?\n")
    bid = int(input("what is your bid?\n"))
    table_of_bids[name] = bid
auction()
any_other_bidders = input("are there any other bidder, type yes or no").lower()
while any_other_bidders == "yes":
    #from replit import clear then use it to clear the screen
    auction()
    any_other_bidders = input("are there any other bidder, type yes or no").lower()

for n in table_of_bids:
    highest_bid = 0
    identity_of_winner = ""
    if table_of_bids[n] > highest_bid:
        highest_bid = table_of_bids[n]
        identity_of_winner = n
print(f"the winner is {identity_of_winner} with a bid of ${highest_bid} ") 
    
