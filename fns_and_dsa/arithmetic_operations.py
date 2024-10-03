def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if (num1 and num2 ) != 0:
                return num1 / num2
            else:
                return f"Cannot divide a number with zero"
        case _ :
            return "Invalid"
