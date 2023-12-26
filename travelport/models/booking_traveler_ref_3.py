from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.discount_card_ref_3 import DiscountCardRef3
from travelport.models.drivers_license_ref_3 import DriversLicenseRef3
from travelport.models.loyalty_card_ref_3 import LoyaltyCardRef3
from travelport.models.payment_ref_4 import PaymentRef4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class BookingTravelerRef3:
    """
    Reference Element for Booking Traveler and Loyalty cards.
    """

    class Meta:
        name = "BookingTravelerRef"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    loyalty_card_ref: list[LoyaltyCardRef3] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCardRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    drivers_license_ref: None | DriversLicenseRef3 = field(
        default=None,
        metadata={
            "name": "DriversLicenseRef",
            "type": "Element",
        },
    )
    discount_card_ref: list[DiscountCardRef3] = field(
        default_factory=list,
        metadata={
            "name": "DiscountCardRef",
            "type": "Element",
            "max_occurs": 9,
        },
    )
    payment_ref: list[PaymentRef4] = field(
        default_factory=list,
        metadata={
            "name": "PaymentRef",
            "type": "Element",
            "max_occurs": 3,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
