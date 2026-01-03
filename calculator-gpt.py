def main():
    name = input('What is your first an second name?').strip().title
    while True:
      a = float(input('What is the first number?', name))
      b = float(input('What is the second number?', name))   
      question = input('What do you want to do with those two numbers?',name).lower().strip()
      if question == '+':
          print(a + b)
      elif question == '-':
          print(a - b)
      elif question == '*':
          print(a * b)
      elif question == '/':
          if b == 0:
              print('Please enter a valid number')
          else:
              print(a / b)
      elif question == '//':
          if b == 0:
              print('Please enter a valid number')
          else:
              print(a // b)
      elif question == '%':
          if b == 0:
              print('Please enter a valid number')
          else:
              print(a % b)
      else:
          print('Enter a valid operator')
    
 
      again = input('Would you like to continue? [yes/no]')
      if again != 'yes':
           print('Goodbye')
           break
        
main()