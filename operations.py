def add_income(budget_data_structure):
    amount=int(input(f"Please enter amount : "))
    description=input(f"Please enter description : ")
    budget_data_structure["transactions"].append({"type":"income","amount":amount,"description":description})
    budget_data_structure["balance"]+=amount
    show_balance(budget_data_structure)
    return budget_data_structure

def add_expense(budget_data_structure):
    amount=int(input(f"Please enter amount : "))
    description=input(f"Please enter description : ")
    budget_data_structure["transactions"].append({"type":"expense","amount":amount,"description":description})
    budget_data_structure["balance"]+=amount
    return budget_data_structure

def show_balance(budget_data_structure):
    print(budget_data_structure["balance"])
    return 

def show_transactions(budget_data_structure):
    for tr in budget_data_structure["transactions"] :
            print (tr)
    return

budget_data_structure = {
    "balance": 500,
    "transactions": [
        {"type": "income", "amount": 1000, "description": "Salary"},
        {"type": "expense", "amount": 500, "description": "Groceries"}
    ]
}
