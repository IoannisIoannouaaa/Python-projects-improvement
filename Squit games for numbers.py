name = input ('What is your full name?').strip().title()
print ('Hello,',name,)
print ('You have to guess the right number if you wanna live')

def get_guess():
    guess = int(input('Enter your guess or else:'))
    return guess
    
    if guess == 20:
        print ('You can live for now')
    else:
       print ('You have been eliminated')
    
get_guess
