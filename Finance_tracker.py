from datetime import date
import json

#the class where we define the transaction and its attributes

categories = ['Food', 'Transport', 'Entertainment', 'Utilities', 'Other']

class Transaction:
        def __init__(self, amount, category, transaction_date):
            if amount <= 0:
                raise ValueError("Amount cannot be negative or zero.")
            self.amount = amount
            self.category = category
            self.date = transaction_date

        def __str__(self):
            return f"Date: {self.date}"

        def to_dict(self):
            return {
                'amount': self.amount,
                'category': self.category,
                'date': self.date.isoformat()
            }
#main program handling user input and transaction management

def main():
    transactions = load_transactions('transactions.json')
    while True:
        question = input("Would you like to add an amount  view transactions  exit  filter by category or filter by date or delete? ").lower()

        if not question:
            print('Input cannot be empty. Please enter a valid response.')
            continue

        if question not in ['add', 'view', 'exit', 'filter', 'filter by date', 'delete']:
            print('Please enter a valid response.')
            continue

        elif question == 'add':
           amount = add_amount()
           category = get_category()
           date = get_date()
           transaction = Transaction(amount, category,date)
           transactions.append(transaction)
           print(f"Added {amount} to {category}.")

        elif question == 'view':
            view_transactions(transactions)

        elif question == 'exit':
            total = calculate_total(transactions)
            print("Transactions summary:")
            for category, amount in total.items():
                print(f"Category: {category}, Total: {amount}")
            save_transactions(transactions, 'transactions.json')
            
            
            print("Exiting the program. Goodbye!")
            break
        elif question == 'filter':
            category = get_category()
            filtered_transactions = [t for t in transactions if t.category == category]
            if not filtered_transactions:
                print(f"No transactions found for category: {category}")
            else:
                view_transactions(filtered_transactions)
                total = sum(t.amount for t in filtered_transactions)
                print(f"Total for {category}: {total}")
        elif question == 'filter by date':
            start_date, end_date = get_date_range()
            filtered_transactions = [t for t in transactions if start_date <= t.date <= end_date]
            if not filtered_transactions:
                print(f"No transactions found between {start_date} and {end_date}.")
            else:
                view_transactions(filtered_transactions)
                total = sum(t.amount for t in filtered_transactions)
                print(f"Total for transactions between {start_date} and {end_date}: {total}")
        elif question == 'delete':
            delete_transaction(transactions)

#Decorator if a transaction amount is negative or zero, raise a ValueError and prevent the transaction from being added to the list of transactions

def require_transaction(func):
    def wrapper(transactions, *args, **kwargs):
        if not transactions:
            raise ValueError("There are no transactions to perform this action.")
        return func(transactions, *args, **kwargs)
    return wrapper

#add a new transaction 

def add_amount():
    while True:
        user_input = input("Enter amount: ").strip()

        if not user_input:
            print("Empty input.")
            continue

        try:
            amount = float(user_input)
            if amount <= 0:
                print("Must be > 0.")
                continue
            return amount
        except ValueError:
            print("Invalid number.")

#get the date of the transaction, with validation for format and future dates

def get_date():
    while True:
        user_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()

        if not user_input:
            return date.today()

        try:
            d = date.fromisoformat(user_input)
            if d > date.today():
                print("Date cannot be in the future.")
                continue
            return d
        except ValueError:
            print("Invalid date format.")

#get the category of the transaction, with validation against predefined categories

def get_category():
    while True:
        category = input("Enter the category for the amount (Food, Transport, Entertainment, Utilities, Other): ").strip().title()
        if category not in categories: 
            print("Invalid category. Please choose from the following: Food, Transport, Entertainment, Utilities, Other.") 
            continue 
        else: 
            return category
        
#view all transactions, or a filtered list of transactions, with a summary of totals by category while indexing    
@require_transaction
def view_transactions(transactions):
    sorted_transactions = sorted(transactions, key=lambda t: t.amount, reverse=True)
    print("Transactions:")
    for i, t in enumerate(sorted_transactions, start=1):
        print(f"{i}. {t}")
#calculate the total amount for each category and return a summary dictionary

def calculate_total(transactions):
    total = {}
    for transaction in transactions:
        category = transaction.category
        amount = transaction.amount
        total[category] = total.get(category, 0) + amount
    return total

#load transactions from a JSON file, converting date strings back to date objects, and return a list of Transaction instances

def load_transactions(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)

        transactions = []
        for item in data:
            item['date'] = date.fromisoformat(item['date'])
            transactions.append(Transaction(**item))

        return transactions

    except FileNotFoundError:
        return []
    
#get the date range for filtering transactions, with validation to ensure the start date is not after the end date
   
def get_date_range():
    while True:
        print("Enter start date:")
        start_date = get_date()

        print("Enter end date:")
        end_date = get_date()

        if start_date > end_date:
            print("Start date cannot be after end date.")
            continue

        return start_date, end_date

def save_transactions(transactions, filename):
    with open(filename, 'w') as file:
        json.dump([t.to_dict() for t in transactions], file, indent=4)

    
#delete a transaction by its index
@require_transaction
def delete_transaction(transactions):

    view_transactions(transactions)
    while True:
        try:
            index = int(input("Enter the number of the transaction to delete (or 0 to cancel): "))
            if index == 0:
                print("Deletion cancelled.")
                return
            elif 1 <= index <= len(transactions):
                deleted = transactions.pop(index - 1)
                save_transactions(transactions, 'transactions.json')
                print(f"Deleted transaction: {deleted}")
                return
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
