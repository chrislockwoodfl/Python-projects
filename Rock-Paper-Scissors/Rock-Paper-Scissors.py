# Rock, Paper, Scissors by Chris Lockwood
#
# This program simulates a game of Rock, Paper, Scissors with the computer.
# The human player is asked for their selection, then the computer chooses one at random.
# If both players choose the same, or the human's choise is invalid,
# the human is prompted to choose again.
# If someone wins, the game stops.

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True: # keep going til someone wins
    human_rps = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

    if human_rps == "0":
        print(rock)
    elif human_rps == "1":
        print(paper)
    elif human_rps == "2":
        print(scissors)
    else:
        print("Invalid choice- choose again")
        continue

    # Computer makes its choice
    rps = random.randint(0,2)
    print("\nComputer chose...")

    if rps == 0:
        print(rock)
        if human_rps == "0":
            print("Tie. Let's play again")
            continue
        elif human_rps == "1":
            print("Paper covers rock. You win!")
        elif human_rps == "2":
            print("Rock breaks scissors. You lose")
    elif rps == 1:
        print(paper)
        if human_rps == "0":
            print("Paper covers rock. You lose")
        elif human_rps == "1":
            print("Tie. Let's play again")
            continue
        elif human_rps == "2":
            print("Scissors cut paper. You win!")
    elif rps == 2:
        print(scissors)
        if human_rps == "0":
            print("Rock breaks scissors. You win!")
        elif human_rps == "1":
            print("Scissors cut paper. You lose")
        elif human_rps == "2":
            print("Tie. Let's play again")
            continue

    # We have a winner, so exit while loop
    break

