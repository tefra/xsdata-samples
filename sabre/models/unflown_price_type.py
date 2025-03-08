from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class UnflownPriceType:
    """
    Totally Unflown Itinerary Price Information.

    Attributes:
        amount:
        currency_code: A currency code (e.g. USD, EUR, PLN)
        decimal_places: Indicates the number of decimal places for a
            particular currency. This is equivalent to the ISO 4217
            standard "minor unit".
    """

    amount: None | Decimal = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "fraction_digits": 3,
        },
    )
    currency_code: None | str = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        },
    )
    decimal_places: None | int = field(
        default=None,
        metadata={
            "name": "DecimalPlaces",
            "type": "Attribute",
        },
    )
