from datetime import date
from pydantic import BaseModel, Field, PositiveFloat


class Holding(BaseModel):
    id: str
    account_id: str
    symbol: str = Field(..., regex=r"^[A-Z.]{1,10}$")
    quantity: PositiveFloat
    cost_basis: PositiveFloat | None = None
    as_of: date
