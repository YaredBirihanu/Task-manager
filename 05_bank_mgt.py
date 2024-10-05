class Account:
    def __init__(self, account_number, account_holder):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}. New Balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self._balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self._balance

    def get_account_info(self):
        return f"Account Number: {self._account_number}, Holder: {self._account_holder}, Balance: {self._balance}"

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self.interest_rate / 100
        self.deposit(interest)

class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, overdraft_limit):
        super().__init__(account_number, account_holder)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= (self._balance + self.overdraft_limit):
            self._balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self._balance}")
        else:
            print("Overdraft limit exceeded or invalid amount.")

# Example usage
savings_account = SavingsAccount("123456", "Alice", 2)
savings_account.deposit(1000)
savings_account.apply_interest()
print(savings_account.get_account_info())

current_account = CurrentAccount("654321", "Bob", 500)
current_account.deposit(200)
current_account.withdraw(600)
print(current_account.get_account_info())