from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.discount_card_ref_4 import DiscountCardRef4
from travelport.models.drivers_license_ref_4 import DriversLicenseRef4
from travelport.models.loyalty_card_ref_4 import LoyaltyCardRef4
from travelport.models.payment_ref_5 import PaymentRef5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class BookingTravelerRef4:
    """
    Reference Element for Booking Traveler and Loyalty cards.
    """
    class Meta:
        name = "BookingTravelerRef"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    loyalty_card_ref: list[LoyaltyCardRef4] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCardRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    drivers_license_ref: None | DriversLicenseRef4 = field(
        default=None,
        metadata={
            "name": "DriversLicenseRef",
            "type": "Element",
        }
    )
    discount_card_ref: list[DiscountCardRef4] = field(
        default_factory=list,
        metadata={
            "name": "DiscountCardRef",
            "type": "Element",
            "max_occurs": 9,
        }
    )
    payment_ref: list[PaymentRef5] = field(
        default_factory=list,
        metadata={
            "name": "PaymentRef",
            "type": "Element",
            "max_occurs": 3,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
