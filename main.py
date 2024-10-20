class BankAccount:
    def __init__(self, name: str):
        self.name = name
        self.balance = 0.0

    def __repr__(self) -> str:
        return f"{self.name}'s account. Balance: ${self.balance:.2f}"

    def show_balance(self) -> str:
        return f"Balance: ${self.balance:.2f}"

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print('Invalid amount')
            return
        else:
            print(f'Depositing: ${amount:.2f}')
            self.balance += amount
            print(self.show_balance())

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            print('Insufficient funds')
            return
        else:
            print(f'Withdrawing: ${amount:.2f}')
            self.balance -= amount
            print(self.show_balance())