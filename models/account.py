from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field


class AccountType(str, Enum):
    brokerage = "brokerage"
    bank = "bank"
    loan = "loan"
    property = "property"


class Account(BaseModel):
    id: str = Field(..., pattern=r"^[A-Za-z0-9_-]{2,32}$")
    name: str
    type: AccountType
    currency: str = Field(default="USD", pattern=r"^[A-Z]{3}$")
    opened: datetime | None = None
