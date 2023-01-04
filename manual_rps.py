# Importing modules necessary
import random

# defining function for computer selection of RPS:
def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

# defining function to obtain user choice between RPS:
def get_user_choice():
    return input('Please choose between Rock, Paper and Scissors: ')