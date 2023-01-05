# Computer Vision - Rock, Paper Scissors (RPS)

Rock, paper, scissors is a classic game in which a player decides to choose rock, paper or scissors at the time of reveal - the rock beats scissors, paper beats rock and scissors beats paper. 

This will be an implementation of the RPS game where a player plays against the computer through the use of the computer camera. 

## Milestone 2

In milestone 2 the task was to create a computer vision system (also known as a model) - that detects whether the player is showing rock, paper or scissors to the camera. To do this:
- Teachable Machine was used to have 4 options: Rock, Paper, Scissors and Nothing and the model was trained to recognise whenever these 4 options were chosen by the user. 
- The more images that were taken the better the model so I iteratively trained the model till I was satisfied that it would recognise each of the 4 options with as much accuracy as possible.
- The model will be used to ensure that the player input through the camera will be recognised without issues so that the player can play against the randomly chosen option by the computer.
- There was no code for this section of the project.

## Milestone 4

This Milestone was to create a Rock-Paper-Scissors game.
- Initially, 2 functions were created: one was to random generate an option between RPS for the computer choice and the other was to creat a function which took in user input for the RPS game.
- A 3rd function was created to run the logic of the game - using if/elif/else statements a function was crated which took in the inputs of the computer and user and compared these to provide various outputs. 
- Finally, a single function called play was created which encompassed all the other functions into 1. This function could now be called to run and play the game of Rock-Paper-Scissors.

```python
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
```

> Insert screenshot of what you have built working.

## Milestone 5

- This Milestone was used to encorporate the image prpject model to play a Rock, Paper, Scissors game with the computer through the use of the webcam.
- Several imports were used in order to be able to run the model and get the images in the right form for processesing.
- The code is split into various functions, each with a specific use:
- get_computer_choice() function was used to get a random choice from the computer between Rock, Paper and Scissors
- get_prediction() function was used to open the webcam, wait 5 seconds per turn and capture an image. The model would then predict in an array the probability that it is each of the options: Rock, Paper, Scissors, Nothing. The index would then be used to assign an object and then that would be the output of the function.
- play_RPS() function was used to run the game logic and keep track of the scores between computer and user until one reaches a score of 3.

```python
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

# A function for randomly choosing between Rock, Paper and Scissors for the computer's choice
def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

# A function which opens the camera, waits 5 seconds from start, obtains the prediction with the highest probability and returns the users choice accordingly
def get_prediction():
    while True:
        start=time.time()
        end=0
        while end - start <=5:
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
def play_RPS():
    computer_wins = 0
    
    user_wins = 0
    
    while computer_wins<=2 and user_wins<=2:
        computer_choice = get_computer_choice()
        print(computer_choice)
        user_choice = get_prediction()
        print(user_choice)
        if computer_choice == user_choice:
            print('It is a tie!')
            print(f"The scores are, computer: {computer_wins} and player: {user_wins}")
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

play_RPS()
```
## Conclusions

- There can be improvements made to the project code by ensuring that when the prediction returns with nothing then the go has to be taken again. 
- The code could also be made more readable by ensuring that each method/ function only completes one task. This way, the code is easier to understand and errors can be found much quicker and easier. 
- However, the code does run smoothly, it provides 5 seconds between each turn just like a real game of Rock, Paper, Scissors and the first to 3 wins between the computer and player, wins the game. 
- The code does run as it joins functions mentioned above together. However, it is also possible to package this up into a Rock, Paper, Scissors class for better code.
- Some added functionality would be to add a replay button, an actual countdown on the camera, adding a visual representation of the computer's choice etc. 