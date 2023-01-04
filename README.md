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

## Milestone n

- Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.

- Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

## Conclusions

- Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

- Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?