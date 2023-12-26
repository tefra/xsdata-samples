from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleRateInfo:
    """Container for adding and modifying Vehicle Rate related information.

    For Modify operation :
    If a value is passed in any of the attributes they will be updated,
    If an empty string is passed then the attributed's value will be deleted,
    If the attribute is not passed no action will be taken.

    Parameters
    ----------
    tour_code
        Tour Number for the Vehicle Booking
    discount_number
        Corporate Discount Number for the Vehicle Booking
    promotional_code
        Promotional Code for the Vehicle Booking
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    tour_code: None | str = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Attribute",
        },
    )
    discount_number: None | str = field(
        default=None,
        metadata={
            "name": "DiscountNumber",
            "type": "Attribute",
            "max_length": 25,
        },
    )
    promotional_code: None | str = field(
        default=None,
        metadata={
            "name": "PromotionalCode",
            "type": "Attribute",
        },
    )
