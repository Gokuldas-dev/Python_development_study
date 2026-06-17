# write a simple program using match  to create simple calclulator
# this is a simple calculator program using match statement 

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))  

operation = input("Enter operation (+, -, *, /): ")

match operation:
    case "+": 
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    case "-": 
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    case "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation. Please enter one of +, -, *, /.")