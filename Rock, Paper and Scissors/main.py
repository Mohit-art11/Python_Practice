import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

        if player == computer:
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("Tie!")

        elif player == "rock":
            if computer == "paper":
                print(f"computer: {computer}")
                print(f"Player: {player}")
                print("You lose!")

            if computer == "scissors":
                print(f"computer: {computer}")
                print(f"Player: {player}")
                print("You win!")

        elif player == "paper":
            if computer == "rock":
                print(f"computer: {computer}")
                print(f"player: {player}")
                print("You win!")

            if computer == "scissors":
                print(f"computer: {computer}")
                print(f"player: {player}")
                print("You lose!")

        elif player == "scissors":
            if computer == "rock":
                print(f"computer: {computer}")
                print(f"player: {player}")
                print("You lose!")

            if computer == "paper":
                print(f"computer: {computer}")
                print(f"player: {player}")
                print("You win!")

    play_again = input("Would you like to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Thanks for playing!")