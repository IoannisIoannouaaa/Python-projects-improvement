def get_guess():
    
    guess = int(input('What is your number?'))
    print('Your number when squared is:',square_guess(guess),)

def square_guess(n):
    return pow(n,2)
    

get_guess()