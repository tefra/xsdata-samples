from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class VoluntaryChangesType:
    """
    Specifies charges and/or penalties associated with making ticket
    changes after purchase.

    Attributes:
        penalty: Specifies penalty charges as either a currency amount
            or a percentage of the fare.
        vol_change_ind: Indicator used to specify whether voluntary
            change and other penalties are involved in the search or
            response.
    """

    penalty: None | VoluntaryChangesType.Penalty = field(
        default=None,
        metadata={
            "name": "Penalty",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    vol_change_ind: None | bool = field(
        default=None,
        metadata={
            "name": "VolChangeInd",
            "type": "Attribute",
        },
    )

    @dataclass
    class Penalty:
        """
        Attributes:
            penalty_type: Indicates the type of penalty involved in the
                search or response.
            departure_status: Identifier used to indicate whether the
                change occurs before or after departure from the origin
                city.
            amount:
            currency_code: A currency code (e.g. USD, EUR, PLN)
            decimal_places: Indicates the number of decimal places for a
                particular currency. This is equivalent to the ISO 4217
                standard "minor unit".
            percent: The penalty charge conveyed as a percent of the
                total fare.
        """

        penalty_type: None | str = field(
            default=None,
            metadata={
                "name": "PenaltyType",
                "type": "Attribute",
            },
        )
        departure_status: None | str = field(
            default=None,
            metadata={
                "name": "DepartureStatus",
                "type": "Attribute",
            },
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
        percent: None | Decimal = field(
            default=None,
            metadata={
                "name": "Percent",
                "type": "Attribute",
                "min_inclusive": Decimal("0.01"),
                "max_inclusive": Decimal("100.00"),
            },
        )
