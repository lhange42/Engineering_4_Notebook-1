# Calculator
# Written by Owen McKenney

def doMath(a, b, operation): # the doMath() function takes inputs a, b, and operation. a is the first number, b is the second number, and operation refers to what operation needs to be performed
    # this series of if statements checks to see what operation needs to be performed
    if operation == 1:
        return str(a + b) # if the input is 1, the doMath() function will return the sum of a and b as a string
    elif operation == 2:
        return str(a - b)
    elif operation == 3:
        return str(a * b)
    elif operation == 4:
        return str(round(a / b, 2)) # to round numbers in python, you do round(number, digits)
    else:
        return str(a % b)

a = int(input("Enter first number : ")) # these two lines get the user input
b = int(input("Enter second number : "))

print("Sum : " + doMath(a,b,1)) # these lines print out the sum, difference, product, quotient, and modulo of the numbers
print("Difference : " + doMath(a,b,2))
print("Product : " + doMath(a,b,3))
print("Quotient : " + doMath(a,b,4))
print("Modulo : " + doMath(a,b,5))
