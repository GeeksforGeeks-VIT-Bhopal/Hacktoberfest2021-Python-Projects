# Python program for simple calculator

# Function to add two numbers
def add(n1, n2):
    return n1 + n2


# Function to subtract two numbers
def subtract(n1, n2):
    return n1 - n2


# Function to multiply two numbers
def multiply(n1, n2):
    return n1 * n2


# Function to divide two numbers
def divide(n1, n2):
    return n1 / n2


def exponent(n1, n2):
    return n1 ** n2

# Condition for running the program multiple times
while True:

    print("Please select operation -\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exponent\n")

    # Take input from the user
    select = int(input("Select operations from 1, 2, 3, 4, 5 : "))

    if 1 <= select <= 5:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if select == 1:
            print(num1, "+", num2, "=", add(num1, num2))

        elif select == 2:
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif select == 3:
            print(num1, "*", num2, "=",multiply(num1, num2))

        elif select == 4:
            print(num1, "/", num2, "=", divide(num1, num2))

        elif select == 5:
            print(num1, "^", num2, "=", exponent(num1, num2))
    else:
        print("Invalid input")
     
    # Asking the using if he wants more calculations
    more = input("Do you want some more calculations?Type 'yes' to continue.\n")
    if more != 'yes':
        print("Hope you got your desired outputs. Thank you for using our calculator.")
        break
