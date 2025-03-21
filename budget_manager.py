# Main data structure that will act as a non-persistent data base.
budget_data_structure = {
 "balance": 500,
 "transactions": [
 {"type": "income", "amount": 1000, "description": "Salary"},
 {"type": "expense", "amount": 500, "description": "Groceries"}
 ]
}

while True:
    print("Select an option:\n 1.Add Income\n 2. Add Expense \n 3.Show Balance \n 4. Show Transaction History \n 5.Exit \n Select An Option:")
    user_choice = input("Please enter a number from the menu option [1-5]")

    match user_choice:
        case 1:
            pass # Add Income = add_income(budget_data_structure , amount_to_add)
        case 2:
            pass # Add Expense = add_expense(budget_data_structure , amount_to_subtract)
        case 3:
            pass # Show Balance = show_balance(budget_data_structure)
        case 4:
            pass # Show Transaction = show_transaction(budget_data_structure)
        case 5:
            pass # Exit
        case _:
            print("Invalid option please re-enter a valid option from the Menu [1-5]")





