# Rock, Paper, Scissors Game

import random

game = ["rock", "paper", "scissors"]
while True:

  ch = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors.\n"))
  if ch > 2:
    print("You entered an invalid number, you lose!")
  else:
    print("You choose", game[ch])
    com_ch = random.randint(0, 2)
    print("Computer chose", game[com_ch])
    if (ch == 0 and com_ch == 1) or (ch == 1 and com_ch == 2) or (ch == 2 and com_ch == 0):
        print("You lose")
    elif (ch == 1 and com_ch == 0) or (ch == 2 and com_ch == 1) or (ch == 0 and com_ch == 2):
        print("You won")
    else:
        print("That's a tie")
  cont = input("Do you wanna play again? Type 'yes' to continue.\n ")
  if cont != 'yes':
    print("Thank you for playing the game.")
    break

