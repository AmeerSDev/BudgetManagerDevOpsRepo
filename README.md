# Budget Manager System

## Overview

In this project, we will design and develop a Python-based budget management program. The system will allow users to track income and expenses, calculate the balance, and display transaction history.

## Project Structure

- **Data Structure**: The budget data will be stored in a dictionary that holds the current balance and a list of transactions.
- **Menu System**: The program will provide the following options:
  1. Add Income
  2. Add Expense
  3. Show Balance
  4. Show Transaction History
  5. Exit

## Data Structure

The chosen data structure for this project is a **dictionary with a transaction list**.

### `budget_data` Structure:
The `budget_data` dictionary contains:
- **balance**: Current balance of the budget (float).
- **transactions**: A list of transactions, where each transaction is a dictionary containing:
  - `type`: A string that can be either "income" or "expense".
  - `amount`: The amount of the transaction (float).
  - `description`: A description of the transaction (string).

Example:
```python
budget_data = {
    "balance": 500.0,
    "transactions": [
        {"type": "income", "amount": 1000.0, "description": "Salary"},
        {"type": "expense", "amount": 500.0, "description": "Groceries"}
    ]
}
