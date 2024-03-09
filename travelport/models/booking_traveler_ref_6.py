from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.discount_card_ref_6 import DiscountCardRef6
from travelport.models.drivers_license_ref_6 import DriversLicenseRef6
from travelport.models.loyalty_card_ref_6 import LoyaltyCardRef6
from travelport.models.payment_ref_7 import PaymentRef7

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class BookingTravelerRef6:
    """
    Reference Element for Booking Traveler and Loyalty cards.
    """

    class Meta:
        name = "BookingTravelerRef"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    loyalty_card_ref: list[LoyaltyCardRef6] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCardRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    drivers_license_ref: None | DriversLicenseRef6 = field(
        default=None,
        metadata={
            "name": "DriversLicenseRef",
            "type": "Element",
        },
    )
    discount_card_ref: list[DiscountCardRef6] = field(
        default_factory=list,
        metadata={
            "name": "DiscountCardRef",
            "type": "Element",
            "max_occurs": 9,
        },
    )
    payment_ref: list[PaymentRef7] = field(
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
