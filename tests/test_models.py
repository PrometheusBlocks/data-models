import pytest
from datetime import datetime, date
from pydantic import ValidationError
from models import Account, Holding, Transaction


def test_account_round_trip():
    data = {
        "id": "acc-01",
        "name": "Test Account",
        "type": "brokerage",
        "currency": "USD",
        "opened": "2020-01-01T12:00:00",
    }
    account = Account(**data)
    dumped = account.model_dump()
    new_account = Account(**dumped)
    assert new_account == account


def test_holding_quantity_must_be_positive():
    with pytest.raises(ValidationError):
        Holding(
            id="h1",
            account_id="a1",
            symbol="AAPL",
            quantity=-10.5,
            cost_basis=100.0,
            as_of="2023-01-01",
        )


def test_transaction_optional_holding_id():
    tx = Transaction(id="t1", account_id="a1", date="2023-01-02", amount=100.5)
    assert tx.holding_id is None
    assert tx.description is None
