# Bank Account Project

This project implements a simple `BankAccount` class in Python. The class allows you to create a bank account, deposit money, withdraw money, and check the account balance.

## Features

- **Create Account**: Initialize a new bank account with a name and a starting balance of $0.00.
- **Deposit**: Add money to the account. The amount must be greater than $0.00.
- **Withdraw**: Remove money from the account. The amount must not exceed the current balance.
- **Show Balance**: Display the current balance of the account.
- **Account Representation**: Provides a string representation of the account showing the account holder's name and the current balance.

## Class Methods

- `__init__(self, name: str)`: Initializes the account with the given name and a balance of $0.00.
- `__repr__(self) -> str`: Returns a string representation of the account.
- `show_balance(self) -> str`: Returns the current balance as a string.
- `deposit(self, amount: float) -> None`: Deposits the specified amount into the account.
- `withdraw(self, amount: float) -> None`: Withdraws the specified amount from the account.
