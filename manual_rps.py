# Importing modules necessary
import random

# # defining function for computer selection of RPS:
# def get_computer_choice():
#     computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
#     return computer_choice

# # defining function to obtain user choice between RPS:
# def get_user_choice():
#     user_choice =  input('Please choose between Rock, Paper and Scissors: ')
#     return user_choice

# # defining a function to get winner between computer and user:
# def get_winner(computer_choice, user_choice):
#     if computer_choice == user_choice:
#         print('It is a tie!')
#     elif computer_choice == 'Rock' and user_choice == 'Scissors':
#         print('You lost')
#     elif computer_choice == 'Paper' and user_choice == 'Rock':
#         print('You lost')
#     elif computer_choice == 'Scissors' and user_choice == 'Paper':
#         print('You lost')
#     else:
#         print('You won!')

# Creating function to encompass all 3 functions above into one:
def play():
    # Asking for user input and storing it
    user_choice =  input('Please choose between Rock, Paper and Scissors: ')
    
    # Generating random computer input and storing it 
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    
    # Control flow generated for RPS game
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

play()