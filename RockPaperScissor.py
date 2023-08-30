# this is a Rock Paper scissor game
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇

user_choice = int(
    input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors ")
)

computer_choice = random.randint(0, 2)

if user_choice == 0:
    if computer_choice == 0:
        print(rock)
        print("Computer choose: \n" + rock)
        print("It is a draw. Try again. ")
    elif computer_choice == 1:
        print(rock)
        print("Computer choose: \n" + paper)
        print("You lose!")
    elif computer_choice == 2:
        print(rock)
print("Computer choose: \n" + scissors) XZAZ                                                                                                                                                                                                                                                                                        AX                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        print("You win!")
    else:
        print("Try again.")

elif user_choice == 1:
    if computer_choice == 0:
        print(paper)
        print("Computer choose: \n" + rock)
        print("You win! ")
    elif computer_choice == 1:
        print(paper)
        print("Computer choose: \n" + paper)
        print("It is a draw. try again.")
    elif computer_choice == 2:
        print(paper)
        print("Computer choose: \n" + scissors)
        print("You win!")
    else:
        print("Try again.")

elif user_choice == 2:
    if computer_choice == 0:
        print(scissors)
        print("Computer choose: \n" + rock)
        print("you lose. ")
    elif computer_choice == 1:
        print(scissors)
        print("Computer choose: \n" + paper)
        print("You lose")
    elif computer_choice == 2:
        print(scissors)
        print("Computer choose: \n" + scissors)
        print("It is a draw. try again.")
    else:
        print("Try again.")
else:
    print("Invalid choice. Try again")
