import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance (consider persisting this)
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit:<amount>, withdraw:<amount>, display")
        sys.exit(1)

    # Split the command and the amount (if provided)
    command, *params = sys.argv[1].split(':')

    # Handle the "display" command that doesn't require an amount
    if command == "display":
        account.display_balance()
        sys.exit(0)

    # Ensure that the amount is provided for deposit and withdraw
    if len(params) == 0:
        print("Error: Missing amount. Example usage: python main.py deposit:100")
        sys.exit(1)

    try:
        amount = float(params[0])  # Convert the amount to a float
    except ValueError:
        print("Error: Amount must be a valid number.")
        sys.exit(1)

    if command == "deposit":
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw":
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Error: Insufficient funds.")
    else:
        print("Error: Invalid command. Available commands: deposit, withdraw, display")

if __name__ == "__main__":
    main()
