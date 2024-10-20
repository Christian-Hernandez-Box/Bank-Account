import pytest
from main import BankAccount

def test_create_account():
    account = BankAccount("Alice")
    assert account.name == "Alice"
    assert account.balance == 0.0

def test_deposit_valid_amount():
    account = BankAccount("Alice")
    account.deposit(100.0)
    assert account.balance == 100.0

def test_deposit_invalid_amount():
    account = BankAccount("Alice")
    account.deposit(-50.0)
    assert account.balance == 0.0

def test_withdraw_valid_amount():
    account = BankAccount("Alice")
    account.deposit(100.0)
    account.withdraw(50.0)
    assert account.balance == 50.0

def test_withdraw_insufficient_funds():
    account = BankAccount("Alice")
    account.deposit(50.0)
    account.withdraw(100.0)
    assert account.balance == 50.0

if __name__ == "__main__":
    pytest.main()