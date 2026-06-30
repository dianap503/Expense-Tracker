# Expense Tracker CLI

A simple and efficient tool for managing personal expenses directly from your terminal, built with Python.

## Features
- **Add**: Add a new expense with a description and an amount.
- **List**: View all expenses in a clean, formatted table.
- **Summary**: Calculate the total expenses (general total or for a specific month).
- **Delete**: Remove an expense based on its unique ID.

## Installation

1. Clone this repository:
   ```bash
   git clone <your-repository-link>
   cd expense-tracker

## Usage
1. Add an Expense:
    ```bash
   python3 expense-tracker.py add --description "Lunch" --amount 20

2. List Expenses
   ```bash
   python3 expense-tracker.py list

3. Summary
   ```bash
   python3 expense-tracker.py summary
   python3 expense-tracker.py summary --month 8

4. Delete an Expense:
   ```bash
   python3 expense-tracker.py delete --id 1

