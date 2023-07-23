from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Yield:
    """An identifier which identifies yield made on original pricing.

    It can be a flat amount of original price. The value of Amount can
    be negative. Negative value implies a discount.

    Parameters
    ----------
    amount
        Yield per passenger level in Default Currency for this entity.
    booking_traveler_ref
        Reference to a booking traveler for which Yield is applied.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )
