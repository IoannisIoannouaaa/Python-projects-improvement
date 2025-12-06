x , y , z = input('Expression:').split(' ')

if y == "+":
   solution = float (x) + float(z)
   print(solution)
elif y == "-":
   solution = float (x) - float(z)
   print(solution)
elif y == "*":
   solution = float (x) * float(z)
   print(solution)

elif y == "/":
   solution = float (x) / float(z)
   print(solution)
