def add_income(budget_data_structure, amount_to_add, description=""):
    """Adds income to the balance and records the transaction."""
    budget_data_structure["balance"] += amount_to_add
    budget_data_structure["transactions"].append({"type": "income", "amount": amount_to_add, "description": description})
    print(f"Income of {amount_to_add} added successfully.")

def add_expense(budget_data_structure, amount_to_subtract, description=""):
    """Subtracts expense from the balance and records the transaction."""
    if amount_to_subtract > budget_data_structure["balance"]:
        print("Insufficient balance for this expense.")
    else:
        budget_data_structure["balance"] -= amount_to_subtract
        budget_data_structure["transactions"].append({"type": "expense", "amount": amount_to_subtract, "description": description})
        print(f"Expense of {amount_to_subtract} added successfully.")

def show_balance(budget_data_structure):
    """Displays the current balance."""
    print(f"Current Balance: {budget_data_structure['balance']}")

def show_transactions(budget_data_structure):
    """Displays all the transactions."""
    if not budget_data_structure["transactions"]:
        print("No transactions recorded.")
    else:
        for transaction in budget_data_structure["transactions"]:
            print(f"Type: {transaction['type']}, Amount: {transaction['amount']}, Description: {transaction['description']}")
