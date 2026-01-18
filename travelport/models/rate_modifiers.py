from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class RateModifiers:
    """
    Parameters
    ----------
    rate_code
    discount_number
    vendor_code
    promotional_code
        Specific coupon or promotion code
    vendor_location_ref
    tour_code
        Tour number or code.  Providers: 1P, 1G, 1V.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    rate_code: None | str = field(
        default=None,
        metadata={
            "name": "RateCode",
            "type": "Attribute",
            "max_length": 10,
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
    vendor_code: None | str = field(
        default=None,
        metadata={
            "name": "VendorCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        },
    )
    promotional_code: None | str = field(
        default=None,
        metadata={
            "name": "PromotionalCode",
            "type": "Attribute",
        },
    )
    vendor_location_ref: None | str = field(
        default=None,
        metadata={
            "name": "VendorLocationRef",
            "type": "Attribute",
        },
    )
    tour_code: None | str = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Attribute",
        },
    )
