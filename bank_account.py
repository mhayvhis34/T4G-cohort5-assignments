class BankAccount:
    # Constructor
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print(f"GHS {amount:.2f} deposited successfully.😊")
            print(f"New Balance: GHS {self.balance:.2f}")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print(f"Transaction failed! {self.name} has insufficient funds.😔")
        else:
            self.balance -= amount
            print(f"GHS {amount:.2f} withdrawn successfully.😊")
            print(f"New Balance: GHS {self.balance:.2f}")

    # Return current balance
    def get_balance(self):
        return self.balance

    # String representation
    def __str__(self):
        return (
    f"\nAccount Holder : {self.name}\n"
    f"Current Balance: GHS {self.balance:.2f}"
)


# Welcome Message
print("=================================")
print(" Welcome to Mavis Bank System 😀")
print("=================================")

# Demonstration

account1 = BankAccount("Nathaniel Narh", 800)
account2 = BankAccount("Ernest Amardi", 1200)

# Transactions
account1.deposit(200)
account1.withdraw(100)

account2.deposit(300)
account2.withdraw(500)

account1.deposit(50)

# Print accounts
print(account1)
print(account2)

# Failed withdrawal
account1.withdraw(1000)