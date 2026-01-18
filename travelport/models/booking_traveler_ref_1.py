from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.discount_card_ref_1 import DiscountCardRef1
from travelport.models.drivers_license_ref_1 import DriversLicenseRef1
from travelport.models.loyalty_card_ref_1 import LoyaltyCardRef1
from travelport.models.payment_ref_1 import PaymentRef1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class BookingTravelerRef1:
    """
    Reference Element for Booking Traveler and Loyalty cards.
    """

    class Meta:
        name = "BookingTravelerRef"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    loyalty_card_ref: list[LoyaltyCardRef1] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCardRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    drivers_license_ref: None | DriversLicenseRef1 = field(
        default=None,
        metadata={
            "name": "DriversLicenseRef",
            "type": "Element",
        },
    )
    discount_card_ref: list[DiscountCardRef1] = field(
        default_factory=list,
        metadata={
            "name": "DiscountCardRef",
            "type": "Element",
            "max_occurs": 9,
        },
    )
    payment_ref: list[PaymentRef1] = field(
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
