# Import the required libraries
import datetime

# Define a dictionary to store user accounts
accounts = {
    "123456789": {"pin": "1234", "balance": 1000, "transaction_history": []},
    "987654321": {"pin": "5678", "balance": 500, "transaction_history": []}
}

# Define a function to authenticate the user
def authenticate_user(account_number, pin):
    """Return True if the user is authenticated, False otherwise"""
    if account_number in accounts and accounts[account_number]["pin"] == pin:
        return True
    else:
        return False

# Define a function to check the account balance
def check_balance(account_number):
    """Return the current account balance"""
    return accounts[account_number]["balance"]

# Define a function to withdraw cash from the account
def withdraw(account_number, amount):
    """Withdraw cash from the account"""
    if amount > accounts[account_number]["balance"]:
        print("Insufficient funds")
    else:
        accounts[account_number]["balance"] -= amount
        accounts[account_number]["transaction_history"].append(("Withdrawal", amount, datetime.datetime.now()))
        print(f"Withdrew ${amount:.2f}")

# Define a function to deposit cash into the account
def deposit(account_number, amount):
    """Deposit cash into the account"""
    accounts[account_number]["balance"] += amount
    accounts[account_number]["transaction_history"].append(("Deposit", amount, datetime.datetime.now()))
    print(f"Deposited ${amount:.2f}")

# Define a function to change the account PIN
def change_pin(account_number, new_pin):
    """Change the account PIN"""
    accounts[account_number]["pin"] = new_pin
    print("PIN changed successfully")

# Define a function to display the transaction history
def display_transaction_history(account_number):
    """Display the transaction history"""
    print("Transaction History:")
    for transaction in accounts[account_number]["transaction_history"]:
        print(f"{transaction[0]}: ${transaction[1]:.2f} on {transaction[2]}")

# Define a function to simulate the ATM machine
def atm_machine():
    print("Welcome to the ATM machine!")
    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")

    if authenticate_user(account_number, pin):
        while True:
            print("\nATM Machine Menu:")
            print("1. Check Balance")
            print("2. Withdraw Cash")
            print("3. Deposit Cash")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print(f"Account Balance: ${check_balance(account_number):.2f}")
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                withdraw(account_number, amount)
            elif choice == "3":
                amount = float(input("Enter amount to deposit: "))
                deposit(account_number, amount)
            elif choice == "4":
                new_pin = input("Enter new PIN: ")
                change_pin(account_number, new_pin)
            elif choice == "5":
                display_transaction_history(account_number)
            elif choice == "6":
                print("Exiting ATM machine. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid account number or PIN. Please try again.")

# Run the ATM machine simulation
atm_machine()