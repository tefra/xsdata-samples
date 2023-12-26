from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PriceRange:
    """
    Parameters
    ----------
    default_currency
        Indicates if the currency code of StartPrice / EndPrice is the
        default currency code
    start_price
        Price range start value
    end_price
        Price range end value
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    default_currency: None | bool = field(
        default=None,
        metadata={
            "name": "DefaultCurrency",
            "type": "Attribute",
        },
    )
    start_price: None | str = field(
        default=None,
        metadata={
            "name": "StartPrice",
            "type": "Attribute",
        },
    )
    end_price: None | str = field(
        default=None,
        metadata={
            "name": "EndPrice",
            "type": "Attribute",
        },
    )
