import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)

    # Check if result is a float (successful division)
    if isinstance(result, float):
        print(f"The result of the division is {result}")
    # else:
    #     print(result)  # This will print the error message from safe_divide

if __name__ == "__main__":
    main()
