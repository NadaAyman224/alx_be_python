def perform_operation( num1, num2, operation):

    match operation:
        case "add":
            addition = str(num1 + num2)
            #print("The result is", addition + ".")
            return addition

        case "subtract":
            subtraction = str(num1 - num2)
            #print("The result is", subtraction + ".")
            return subtraction

        case "multiply":
            mul = str(num1 * num2)
            #print("The result is", mul + ".")
            return mul

        case "divide":
            if num2 == 0:
                print("Cannot divide by zero.")
            else :
                div = str(num1 / num2)
                #print("The result is", div + ".")
                return div
    