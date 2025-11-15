num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        addition = str(num1 + num2)
        print("The result is", addition + ".")

    case "-":
        subtraction = str(num1 - num2)
        print("The result is", subtraction + ".")

    case "*":
        mul = str(num1 * num2)
        print("The result is", mul + ".")

    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else :
            div = str(num1 / num2)
            print("The result is", div + ".")

    
    