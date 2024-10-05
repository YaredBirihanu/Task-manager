from datetime import datetime

class Transaction:
    def __init__(self, amount, category, date, transaction_type):
        self.amount = amount
        self.category = category
        self.date = date
        self.transaction_type = transaction_type  # 'income' or 'expense'

    def __str__(self):
        return f"{self.transaction_type.capitalize()}: {self.amount} in {self.category} on {self.date.strftime('%Y-%m-%d')}"


class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        print(f"Transaction added: {transaction}")

    def remove_transaction(self, transaction_index):
        if 0 <= transaction_index < len(self.transactions):
            removed = self.transactions.pop(transaction_index)
            print(f"Transaction removed: {removed}")
        else:
            print("Transaction index out of range.")

    def summarize(self):
        income = sum(t.amount for t in self.transactions if t.transaction_type == 'income')
        expenses = sum(t.amount for t in self.transactions if t.transaction_type == 'expense')
        balance = income - expenses
        return {
            'Total Income': income,
            'Total Expenses': expenses,
            'Balance': balance,
        }

    def list_transactions(self):
        return [str(t) for t in self.transactions]


class FrontendManager:
    def __init__(self):
        self.tracker = FinanceTracker()

    def run(self):
        while True:
            print("\n--- Personal Finance Tracker ---")
            print("1. Add Transaction")
            print("2. Remove Transaction")
            print("3. View Summary")
            print("4. List Transactions")
            print("5. Exit")
            choice = input("Choose an option (1-5): ")

            if choice == '1':
                amount = float(input("Enter amount: "))
                category = input("Enter category (e.g., Food, Salary): ")
                date_str = input("Enter date (YYYY-MM-DD): ")
                date = datetime.strptime(date_str, '%Y-%m-%d')
                transaction_type = input("Enter type (income/expense): ").lower()
                transaction = Transaction(amount, category, date, transaction_type)
                self.tracker.add_transaction(transaction)

            elif choice == '2':
                self.tracker.list_transactions()
                index = int(input("Enter the index of the transaction to remove: "))
                self.tracker.remove_transaction(index)

            elif choice == '3':
                summary = self.tracker.summarize()
                print("\nFinancial Summary:")
                for key, value in summary.items():
                    print(f"{key}: {value}")

            elif choice == '4':
                transactions = self.tracker.list_transactions()
                print("\nTransactions:")
                for i, transaction in enumerate(transactions):
                    print(f"{i}: {transaction}")

            elif choice == '5':
                print("Exiting the system.")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    frontend = FrontendManager()
    frontend.run()