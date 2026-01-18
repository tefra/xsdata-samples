from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class AirFeeType:
    """
    Defines the data fields available for the fees.

    Attributes:
        value:
        fee_code: Identifies the code for the fee.
        amount:
        currency_code: A currency code (e.g. USD, EUR, PLN)
        decimal_places: Indicates the number of decimal places for a
            particular currency. This is equivalent to the ISO 4217
            standard "minor unit".
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    fee_code: str = field(
        metadata={
            "name": "FeeCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        }
    )
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
