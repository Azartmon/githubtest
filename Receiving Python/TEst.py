# Testing of python skills.
# Requirement:  you will write a roll dice game, one player is computer, another is human.  The bigger number will win
# the game.  The code need have try catch block, and it inputs and outputs. and it need has a prompt of yes or no for
# continue the game.

import random

def game():
    def get_numbers():
        dice_faces = [1, 2, 3, 4, 5, 6]
        player_number = random.choice(dice_faces)
        computer_choice = random.choice(dice_faces)
        choices = {"player": player_number, "computer": computer_choice}
        return choices

    def check_win(player, computer):
        print(f"You rolled {player}, computer rolled {computer}")
        if player == computer:
            return "It's a tie!"
        if player > computer:
            return "You won!"
        if player < computer:
            return "Conputer won!"

    choices = get_numbers()
    result = check_win(choices["player"], choices["computer"])
    print(result)
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        game()

if __name__ == "__main__":
    game()