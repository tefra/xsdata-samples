from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.cabin_class_2 import CabinClass2
from travelport.models.seat_attributes_2 import SeatAttributes2
from travelport.models.type_key_based_reference_2 import TypeKeyBasedReference2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class ServiceData2:
    """
    Parameters
    ----------
    seat_attributes
    cabin_class
    ssrref
        References to the related SSRs. At present, only reference to ASVC
        SSR is supported. Supported providers are 1G/1V/1P/1J
    data
        Data that specifies the details of the merchandising offering (e.g.
        seat number for seat service)
    air_segment_ref
        Reference to a segment if the merchandising offering only pertains
        to that segment. If no segment reference is present this means this
        offering is for the whole itinerary.
    booking_traveler_ref
        Reference to a passenger if the merchandising offering only pertains
        to that passenger. If no passenger reference is present this means
        this offering is for all passengers.
    stop_over
        Indicates that there is a significant delay between flights (usually
        12 hours or more)
    traveler_type
        Passenger Type Code.
    emdsummary_ref
        Reference to the corresponding EMD issued. Supported providers are
        1G/1V/1P/1J
    emdcoupon_ref
        Reference to the corresponding EMD coupon issued. Supported
        providers are 1G/1V/1P/1J
    """

    class Meta:
        name = "ServiceData"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    seat_attributes: None | SeatAttributes2 = field(
        default=None,
        metadata={
            "name": "SeatAttributes",
            "type": "Element",
        },
    )
    cabin_class: None | CabinClass2 = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Element",
        },
    )
    ssrref: list[TypeKeyBasedReference2] = field(
        default_factory=list,
        metadata={
            "name": "SSRRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    data: None | str = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Attribute",
        },
    )
    air_segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "AirSegmentRef",
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
    stop_over: bool = field(
        default=False,
        metadata={
            "name": "StopOver",
            "type": "Attribute",
        },
    )
    traveler_type: None | str = field(
        default=None,
        metadata={
            "name": "TravelerType",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        },
    )
    emdsummary_ref: None | str = field(
        default=None,
        metadata={
            "name": "EMDSummaryRef",
            "type": "Attribute",
        },
    )
    emdcoupon_ref: None | str = field(
        default=None,
        metadata={
            "name": "EMDCouponRef",
            "type": "Attribute",
        },
    )
