from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class CurrencyRateConversion:
    """
    Currency rate conversion from the supplier’s source currency to a
    preferred currency.

    For hotels, applicable only to Hotel Super Shopper (1G/1V).

    Parameters
    ----------
    rate_conversion
        Rate multiplier from the supplier’s local or quoted currency to
        requested currency. Used to derive the requested conversion currency
        amount.
    source_currency_code
        3-character ISO currency code for supplier's local or quoted
        currency.
    requested_currency_code
        3-character ISO currency code for the requester's preferred currency
    decimal_places
        The number of decimal places for the requested currency at
        conversion.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    rate_conversion: None | float = field(
        default=None,
        metadata={
            "name": "RateConversion",
            "type": "Attribute",
        },
    )
    source_currency_code: None | str = field(
        default=None,
        metadata={
            "name": "SourceCurrencyCode",
            "type": "Attribute",
            "length": 3,
        },
    )
    requested_currency_code: None | str = field(
        default=None,
        metadata={
            "name": "RequestedCurrencyCode",
            "type": "Attribute",
            "length": 3,
        },
    )
    decimal_places: None | int = field(
        default=None,
        metadata={
            "name": "DecimalPlaces",
            "type": "Attribute",
        },
    )
