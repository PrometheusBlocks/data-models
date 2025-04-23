# data-models

Shared Pydantic v2 record types (Account, Holding, Transaction).

## Installation

```bash
pip install git+https://github.com/PrometheusBlocks/data-models.git
```

## Usage

```python
from models import Account, AccountType

account = Account(
    id="acc-01",
    name="My Brokerage Account",
    type=AccountType.brokerage,
    currency="USD",
    opened="2020-01-01T00:00:00"
)
print(account)
```

## Entry Points

| Entry Point | Description                                          |
|-------------|------------------------------------------------------|
| Account     | Account model representing an account with metadata. |
| Holding     | Holding model linking a symbol to an account.        |
| Transaction | Transaction model for account cash flows.            |

## Running Tests

```bash
pip install -r requirements.txt pytest
pytest -q
```

## Versioning & Token-Budget

This utility follows [Semantic Versioning](https://semver.org/). CI enforces a token budget of 200,000 via `scripts/token_check.py`.