def calculator():
    num1 = float(input("Enter the first number :"))
    num2 = float(input("Enter the second number :"))
    operation=input("choose an operation (+,-,*,/):")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*": 
        result = num1 * num2
    elif operation == "/": 
        result = num1 / num2
    else:
        print("Invalid operation selected.")
        return
    print("The result is: ",result)
    
calculator()    
