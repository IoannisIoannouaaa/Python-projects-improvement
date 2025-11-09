name = input('What is your full name?').strip().title()
print(f'Well hello, {name}')
print('Welcome to the number show where a wrong answer costs your life')


def get_guess():
    guess = int(input('Enter your guess here:'))
    return guess
    

def main ():
    guess = get_guess()
    print(guess)
    if guess == 50:
        print('You can live, for now',name,)
    else :
        print('You have been eliminated')
    
main()
    
