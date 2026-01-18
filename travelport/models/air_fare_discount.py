from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_fare_discount import TypeFareDiscount

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AirFareDiscount:
    """
    Fare Discounts.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    percentage: None | float = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Attribute",
        },
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        },
    )
    discount_method: None | TypeFareDiscount = field(
        default=None,
        metadata={
            "name": "DiscountMethod",
            "type": "Attribute",
        },
    )
