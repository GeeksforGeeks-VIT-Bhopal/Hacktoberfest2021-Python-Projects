def calculator():
    var1 = float(input("Enter number 1 - "))
    var2 = float(input("Enter number 2 - "))
    operation = input("Enter the sign of operation you want to perform - ")

    if operation=="+" :
        print("Sum of these two numbers are = " + str(var1+var2))
    elif operation=="-":
        print("Difference of these two numbers are = " + str(var1-var2))
    elif operation=="*":
        print("Product of these two numbers are = " + str(var1*var2))
    elif operation=="/":
        print("Quotient of these two numbers are = " + str(var1/var2))
    else:
        print("Invalid Expression given by the user")
calculator()   
