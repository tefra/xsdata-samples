from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Adjustment:
    """
    An indentifier which indentifies adjustment made on original pricing.

    It can a flat amount or percentage of original price. The value of
    Amount/Percent can be negetive. Negative value implies a discount.

    Parameters
    ----------
    amount
        Implies a flat amount to be adjusted. Negetive value implies a
        discount.
    percent
        Implies an adjustment to be made on original price. Negetive value
        implies a discount.
    adjusted_total_price
        The adjusted price after applying adjustment on Total price
    approximate_adjusted_total_price
        The Converted adjusted total price in Default Currency for this
        entity.
    booking_traveler_ref
        Reference to a booking traveler for which adjustment is applied.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
        },
    )
    percent: None | float = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Element",
        },
    )
    adjusted_total_price: None | str = field(
        default=None,
        metadata={
            "name": "AdjustedTotalPrice",
            "type": "Attribute",
            "required": True,
        },
    )
    approximate_adjusted_total_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateAdjustedTotalPrice",
            "type": "Attribute",
        },
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        },
    )
