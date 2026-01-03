import random
random_guess = random.randint(1,100)
name = input('What is your full name?').strip().title()
print(f'Well hello, {name}')
print('Welcome to the number show')

def get_guess():
    guess = int(input('Enter your guess here:'))
    return guess
    
def main ():
    guess = get_guess()
    while guess != random_guess:
        if guess > random_guess:
            print('Too high try again')
        else :
            print('Too low try again')
        guess = get_guess()
    print('You found it!')
    
main()