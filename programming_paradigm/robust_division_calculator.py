def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        return numerator / denominator

    except ZeroDivisionError as z:
        print(z)

    except ValueError:
        print("Error: Please enter numeric values only.")
        


