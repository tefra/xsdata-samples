from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.loyalty_card_ref_1 import LoyaltyCardRef1

__NAMESPACE__ = "http://www.travelport.com/schema/cruise_v52_0"


@dataclass
class CruiseBookingTravelerRef:
    """
    Reference Element for Booking Traveler and Loyalty cards.

    Parameters
    ----------
    loyalty_card_ref
    key
    waiver_indicator
        Indicates Passenger accepts/rejects waiver or insurance from vendor.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    loyalty_card_ref: list[LoyaltyCardRef1] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCardRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    waiver_indicator: None | bool = field(
        default=None,
        metadata={
            "name": "WaiverIndicator",
            "type": "Attribute",
        },
    )
