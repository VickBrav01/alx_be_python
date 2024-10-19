class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static Method to add two numbers
    @staticmethod
    def add(a, b):
        return a + b

    # Class Method to multiply two numbers and reference a class attribute
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Testing the Calculator class
def main():
    # Using the static method
    sum_result = Calculator.add(5, 3)
    print(f"Sum of 5 and 3: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(4, 7)
    print(f"Product of 4 and 7: {product_result}")


if __name__ == "__main__":
    main()
