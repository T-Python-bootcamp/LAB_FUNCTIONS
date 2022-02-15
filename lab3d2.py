def myFunc(number):
   result = ""
   for num in range(number,0,-1):
       for n in range(num,0,-1):
           result += f"{n}"
       print(result)
       result=""


myFunc(5)