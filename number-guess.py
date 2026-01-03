import random

random_guess = random.randint(1,100)

guess = int(input('What is your guess?'))

while guess != random_guess:
    if guess > random_guess:
        print('Too high try again')
    else :
        print('Too low try again')
    guess = int(input('What is your guess?'))

        
print('You found it!')



    

