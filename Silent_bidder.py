# import os for mac ios to clear the console
import os


def clear_screen():
    os.system("clear")


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


# HINT: You can call clear() to clear the output in the console.f
def greeting():
    print(logo)
    print("Welcome to the secret auction program.")


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with bid of {highest_bid}")


bid_dict = {}
greeting()
Bidding_finished = False
while not Bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "))
    bid_dict[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        Bidding_finished = True
        clear_screen()
        find_highest_bidder(bid_dict)

    else:
        clear_screen()
