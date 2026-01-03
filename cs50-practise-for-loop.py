def main():
    n = get_number()
    meow(n)
    
def get_number():
    while True:
        n = int(input('What is n?'))
        if n > 0:
            break
    return n


def meow(n):
    for i in range(n):
        print('meow')
        
main()