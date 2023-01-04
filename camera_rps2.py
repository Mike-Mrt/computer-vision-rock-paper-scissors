import random
import cv2
import time
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

x = True
while x:
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    user_choice=np.argmax(prediction)
    if user_choice == 0:
        print('Rock')
        user_choice='Rock'
        x = False
    elif user_choice == 1:
        print('Paper')
        user_choice='Paper'
        x = False
    elif user_choice == 2:
        print('Scissors')
        user_choice='Scissors'
        x = False
    elif user_choice == 3:
        print('Nothing')
        user_choice='Nothing'
        
# print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break       
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
    
# Generating random computer input and storing it 
computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
print(computer_choice)
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

