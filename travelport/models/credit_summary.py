from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class CreditSummary:
    """
    Credit summary associated with the account.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    currency_code: None | str = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Attribute",
            "length": 3,
        },
    )
    current_balance: None | Decimal = field(
        default=None,
        metadata={
            "name": "CurrentBalance",
            "type": "Attribute",
            "required": True,
        },
    )
    initial_credit: None | Decimal = field(
        default=None,
        metadata={
            "name": "InitialCredit",
            "type": "Attribute",
            "required": True,
        },
    )
