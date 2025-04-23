from datetime import date
from pydantic import BaseModel


class Transaction(BaseModel):
    id: str
    account_id: str
    holding_id: str | None = None
    date: date
    amount: float
    description: str | None = None
