import pytest
from main import add, BankAccount, divide
from unittest.mock import patch

def test_should_add_two_numbers():
    # Setup 
    # Act
    totalSum = add(5, 5)
    # Assert - Jämförelse mellan förväntat värde och det faktiska värdet, ska resultera i true/false
    assert totalSum == 10

def test_should_deposit_to_bank_account():
    account = BankAccount("Ada", 100)
    account.deposit(50)
    assert account.saldo == 150

def test_should_withdraw_successfully():
    account = BankAccount("Ada", 100)
    result = account.withdraw(50)
    assert result is True
    assert account.saldo == 50

def test_should_not_withdraw_if_amount_exceeds_saldo():
    account = BankAccount("Ada", 100)
    result = account.withdraw(200)
    assert result == False
    assert account.saldo == 100

def test_should_divide_by_ten():
    with patch("builtins.input", return_value=2): # Mocka input-funktionen så vi inte behöver manuellt skriva in ett värde
        result = divide()
    assert result == 5

def test_should_raise_error_if_divide_by_zero():
    with patch("builtins.input", return_value=0):
        with pytest.raises(ZeroDivisionError):
            divide()