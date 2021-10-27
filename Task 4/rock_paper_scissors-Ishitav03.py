import random

while True:
    Your_choices = ["rock","paper","scissors"]

    computer = random.choice(Your_choices)
    player = None

    while player not in Your_choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("It's a Tie!")

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You Lose!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("Yay! You Win.")

    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You Lose!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("Yay! You Win.")

    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("Yay!You win.")

    play_again = input("Play again? (y/n): ").lower()

    if play_again != "y":
        break

print("BYE!")