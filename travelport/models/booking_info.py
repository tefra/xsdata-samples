from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BookingInfo:
    """
    Links segments and fares together.

    Parameters
    ----------
    booking_code
    booking_count
        Seat availability of the BookingCode
    cabin_class
    fare_info_ref
    segment_ref
    coupon_ref
        The coupon to which that booking is relative (if applicable)
    air_itinerary_solution_ref
        Reference to an Air Itinerary Solution
    host_token_ref
        HostToken Reference for this segment and fare combination.
    tax_info_ref
        TaxInfo Reference for booking info and tax info combination.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    booking_code: None | str = field(
        default=None,
        metadata={
            "name": "BookingCode",
            "type": "Attribute",
            "required": True,
        }
    )
    booking_count: None | str = field(
        default=None,
        metadata={
            "name": "BookingCount",
            "type": "Attribute",
        }
    )
    cabin_class: None | str = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
        }
    )
    fare_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
            "required": True,
        }
    )
    segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        }
    )
    coupon_ref: None | str = field(
        default=None,
        metadata={
            "name": "CouponRef",
            "type": "Attribute",
        }
    )
    air_itinerary_solution_ref: None | str = field(
        default=None,
        metadata={
            "name": "AirItinerarySolutionRef",
            "type": "Attribute",
        }
    )
    host_token_ref: None | str = field(
        default=None,
        metadata={
            "name": "HostTokenRef",
            "type": "Attribute",
        }
    )
    tax_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "TaxInfoRef",
            "type": "Attribute",
        }
    )
