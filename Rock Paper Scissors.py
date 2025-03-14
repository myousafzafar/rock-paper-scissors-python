
import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, or scissors): ")
    valid_options = ['rock', 'paper', 'scissors']
    computed_choice = random.choice(valid_options)
    choices_dict = {'player': player_choice, 'computer': computed_choice}
    return choices_dict

def check_win(player_choice, computer_choice):
    print(f"You chose {player_choice}, computer chose {computer_choice}")
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock":
        if computer_choice == "paper":
            print("Paper wraps rock! You lose!")
        else:
            print("Rock breaks scissors. You win!")
    elif player_choice == "paper":
        if computer_choice == "scissors":
            print("Scissors cut paper! You lose!")
        else:
            print("Paper wraps rock. You win!")
    elif player_choice == "scissors":
        if computer_choice == "rock":
            print("Rock breaks scissors! You lose!")
        else:
            print("Scissors cut paper. You win!")
    else:
        print("Invalid choice by the player, please try again.") 
        choices = get_choices()
        check_win(choices['player'], choices['computer']) 


choices = get_choices()

check_win(choices['player'], choices['computer'])