import random

options = ("rock","paper", "scissors")
playing = True

while playing:
    player = None
    computer = random.choice(options)

    while player not in options: #It checks whether the value of the variable player is not present in the options list
        player = input("Enter your choice (Rock, Paper, Scissors): ").lower()


    print("Player: " + player.capitalize())

    print("Computer: " + computer.capitalize())

    #print(f"Player: {player}")It is another method to print
    #print(f" Computer: {computer}")

    if player == computer:
        print("It's a tie between you and computer.!")
    elif player == "Rock" and computer == "Scissors":
        print("You win the game.!!")
    elif player == "Paper" and computer == "Rock":
        print("You win the game.!!")
    elif player == "Scissors" and computer == "Paper":
        print("You win the game.!!")
    else:
        print("You lose the game..!! Try again.!")

    play_again = input("Do you want to play again.? (yes/no/y/n): ").lower()
    if  play_again not in ["yes","y"]:
        playing = False
print("Thank you for playing with me.!!")

