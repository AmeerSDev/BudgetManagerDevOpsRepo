import operations

# Main data structure that will act as a non-persistent data base.
budget_data_structure = {
    "balance": 500,
    "transactions": [
        {"type": "income", "amount": 1000, "description": "Salary"},
        {"type": "expense", "amount": 500, "description": "Groceries"}
    ]
}

while True:
    print("Select an option:\n 1. Add Income\n 2. Add Expense \n 3. Show Balance \n 4. Show Transaction History \n 5. Exit \n Select An Option:")
    user_choice = input("Please enter a number from the menu option [1-5]: ")

    match user_choice:
        case "1":
           
                #amount_to_add = float(input("Enter the amount of income you would like to add: "))
                #description = input("Enter a description (optional): ")
                operations.add_income(budget_data_structure)
        case "2":
           
                #amount_to_subtract = float(input("Enter an expense amount you recently spent: "))
                #description = input("Enter a description (optional): ")
                operations.add_expense(budget_data_structure)
           
        case "3":
            print("Showing Balance..")
            operations.show_balance(budget_data_structure)
        case "4":
            print("Showing Transactions..")
            operations.show_transactions(budget_data_structure)
        case "5":
            print("Exiting..")
            break  # Exit the loop and end the program
        case _:
            print("Invalid option. Please re-enter a valid option from the Menu [1-5]")
