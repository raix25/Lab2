x= float(input("Enter any number:"))
y = float(input("Enter any number:"))

print(f' The addition of the number is {x+y}')
print(f' The subtraction from 2nd number from 1st is {y-x}')
print(f' The multiplication of the numbers is {x*y}')
if y==0: print(" unable to do the calculation") 
else: print(f' The division of the number is {x/y:.2f}') 
if y==0: print(" unable to do the calculation")
else: print(f' The integer division of the number is {x//y}')
if y==0: print(" unable to do the calculation")
else: print(f' The remainder of the number is {x%y} ')
print(f' The exponent of the given number is {x**y} ')