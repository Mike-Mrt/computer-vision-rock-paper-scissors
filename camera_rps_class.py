# Importing all required modules
import random
import cv2
import time
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
user_choice=["Rock", "Paper", "Scissors", "Nothing"]

# Creating class for RPS game
class RockPaperScissors:
    '''
    This will be a rock, paper, scissors game that will use the computer camera to take in the user choice and play against the computer.
    It will ask for numer of wins required to win the game and how many seconds between each round.
    '''
    def __init__(self,num_wins, show_time):
        self.num_wins = num_wins
        self.show_time = show_time
    
    # A function for randomly choosing between Rock, Paper and Scissors for the computer's choice
    def get_computer_choice(self):
        return random.choice(['Rock', 'Paper', 'Scissors'])
    
    # A function which opens the camera, waits 5 seconds from start, obtains the prediction with the highest probability and returns the users choice accordingly
    def get_prediction(self):
        while True:
            start=time.time()
            end=0
            while end - start <=self.show_time:
                ret, frame = cap.read()
                resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                image_np = np.array(resized_frame)
                normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                data[0] = normalized_image
                prediction = model.predict(data)
                cv2.imshow('frame', frame)
                # Press q to close the window
                prediction=np.argmax(prediction)
                user=user_choice[prediction]
                end=time.time()
            return user
    
    # Function which initiates the game and includes the above 2 functions. 
    # Keeps track of the scores and a hand is played every 5 seconds.

def play_rps():
    game=RockPaperScissors(3,5)
    computer_wins=0
    user_wins=0
    while computer_wins<=(game.num_wins-1) and user_wins<=(game.num_wins-1):
        computer_choice = game.get_computer_choice()
        user_choice = game.get_prediction()
        print(user_choice)
        if computer_choice == user_choice:
            print('It is a tie!')
            print(f"The scores are, computer: {computer_wins} and player: {user_wins}")
        elif user_choice == 'Nothing':
            continue
        elif computer_choice == 'Rock' and user_choice == 'Scissors':
            print('You lost')
            computer_wins+=1
            print(f"The scores are, computer: {computer_wins} and player: {user_wins}")
        elif computer_choice == 'Paper' and user_choice == 'Rock':
            print('You lost')
            computer_wins+=1
            print(f"The scores are, computer: {computer_wins} and player: {user_wins}")
        elif computer_choice == 'Scissors' and user_choice == 'Paper':
            print('You lost')
            computer_wins+=1
            print(f"The scores are, computer: {computer_wins} and player: {user_wins}")
        else:
            print('You won!')
            user_wins+=1
            print(f"The scores are, computer: {computer_wins} and player: {user_wins}")

if __name__ == '__main__':
    play_rps()
        

