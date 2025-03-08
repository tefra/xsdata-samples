from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class ExchangeFareType:
    """
    Attributes:
        base_fare_amount: Base fare amount
        non_refundable_amount: Non-refundable Base Fare Amount. Currency
            is defined by @BaseFareCurrency.
        base_fare_currency: Base fare currency
        fare_calc_currency: Fare calc currency
        validating_carrier: Validating carrier
        roe: Rate of Exchange override (note: doesn't need to be
            specified if FareCalc currency and BaseFare currency is the
            same).
    """

    base_fare_amount: None | Decimal = field(
        default=None,
        metadata={
            "name": "BaseFareAmount",
            "type": "Attribute",
            "required": True,
            "fraction_digits": 3,
        },
    )
    non_refundable_amount: None | Decimal = field(
        default=None,
        metadata={
            "name": "NonRefundableAmount",
            "type": "Attribute",
            "fraction_digits": 3,
        },
    )
    base_fare_currency: None | str = field(
        default=None,
        metadata={
            "name": "BaseFareCurrency",
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z]{3}",
        },
    )
    fare_calc_currency: None | str = field(
        default=None,
        metadata={
            "name": "FareCalcCurrency",
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z]{3}",
        },
    )
    validating_carrier: None | str = field(
        default=None,
        metadata={
            "name": "ValidatingCarrier",
            "type": "Attribute",
            "pattern": r"[0-9A-Z]{2,3}",
        },
    )
    roe: None | float = field(
        default=None,
        metadata={
            "name": "ROE",
            "type": "Attribute",
        },
    )
