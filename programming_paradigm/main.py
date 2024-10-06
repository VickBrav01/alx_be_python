import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    try:
        numerator = sys.argv[1]
        denominator = sys.argv[2]

    except ValueError:
        sys.exit(1)

    result = safe_divide(numerator, denominator)

    if result is not None:
        print(f"The result of the division is {result}")

if __name__ == "__main__":
    main()