import numpy as np
number = np.random.randint(1, 101) # guessing the number    

    #number of attempts
count = 0
while True:
  
    count+=1
    predict_number=int(input('Guess the number from 1 to 101: '))    
    if predict_number>number:
        print ('The number must be less than')
    elif predict_number<number:
        print ('The number must be greater than')
    else:
        print(f'You guessed the number! this number is = {number} in {count} attempts')
        break 

    