# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations
#  to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock



import sys

player1 = input("Please enter your name: ")
player2 = input( "Enter your name too: ")
Player1_choice = input("%s, Choose rock paper or scissors:" %player1)
Player2_choice = input("%s,Choose rock,paper or scissors:" %player2)


def compare(choice1,choice2):
    if choice1 == choice2:
        return "It is a tie!"
    elif choice1 == "rock":
        if choice2 == "scissors":
            return "Rock wins!"
        else:
            return "Paper wins!"
    elif choice1 == "Paper":
        if choice2 == "rock":
            return "Paper wins!"
        return "scissors wins!"
    else:
        return "invalid input, please try again."
        sys.exit()


print(compare(Player1_choice,Player2_choice))
