# Importing modules necessary
import random

# defining function for computer selection of RPS:
def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

# defining function to obtain user choice between RPS:
def get_user_choice():
    return input('Please choose between Rock, Paper and Scissors: ')

# defining a function to get winner between computer and user:
def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print('It is a tie!')
    elif computer_choice == 'Rock' and user_choice == 'Scissors':
        print('You lost')
    elif computer_choice == 'Paper' and user_choice == 'Rock':
        print('You lost')
    elif computer_choice == 'Scissors' and user_choice == 'Paper':
        print('You lost')
    else:
        print('You won!')