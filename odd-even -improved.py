def main():
    x = float(input('What is x?'))
    if is_even(x):
        print(' x is an even number')
    else:
        print('x is an odd number')
        
def is_even(n):
    return True if n%2 == 0 else  False
main()
    