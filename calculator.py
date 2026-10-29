while True: 
    command = input(" Enter'break' to stop, or press Enter to continue.")
    if command == "break":
        break
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    choose = input("Choose an operation (+, -, *, /,%): ")

    if choose == "+":
        print(f"{number1} + {number2} is {number1 + number2}.")
    elif choose == "-":
        print(f"{number1} - {number2} is {number1 - number2}.")
    elif choose == "*":
        print(f"{number1} * {number2} is {number1 * number2}.")
    elif choose == "/":
        if number2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"{number1} / {number2} is {number1 / number2}.")
    elif choose == "%":
        if number2 == 0:
            print("Error: Remainder by zero is not allowed.")
        else:
            print(f"{number1} % {number2} is {number1 % number2}.")
    else:
        print("Invalid operation.")