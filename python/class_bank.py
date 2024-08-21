class BankAccount:
    def __init__(self):
        self.balance = 0
        print("Welcome to the deposit and withdraw machine")

    def deposit(self):
        amount = int(input("Enter the amount you want to deposit: "))
        self.balance += amount
        print("Your balance is: ", self.balance)

    def withdraw(self):
        amount = int(input("Enter the amount you want to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. Your remaining balance is: {self.balance}")
        else:
            print("Insufficient balance")

    def display(self):
        print("The current balance is: ", self.balance)

# Create an instance of BankAccount
s = BankAccount()

# Example usage:
s.deposit()
s.withdraw()
s.display()
