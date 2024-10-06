def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        try: 
            return numerator / denominator
        except ValueError:
            print("Error: Please enter numeric values only.")

    except ZeroDivisionError as z:
        print(z)




