from bank_account import BankAccount


class SavingsAccount(BankAccount):

    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    # Apply interest
    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.deposit(interest)

    # Override __str__
    def __str__(self):
        return (
            f"SavingsAccount[{self.name}] | "
            f"Balance: GHS {self.balance:.2f} | "
            f"Rate: {self.interest_rate}%"
        )


# Demonstration

savings = SavingsAccount("Audrey", 1500, 7)

savings.deposit(500)
savings.deposit(200)

print("Before interest:")
print(savings)

savings.apply_interest()

print("\nAfter interest:")
print(savings)

savings.withdraw(300)

print("\nAfter withdrawal:")
print(savings)