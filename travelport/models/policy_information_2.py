from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_segment_policy import TypeSegmentPolicy

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class PolicyInformation2:
    """
    Policy information associated with SavedTrip.

    Parameters
    ----------
    air_policy
    rail_policy
    hotel_policy
    vehicle_policy
    booking_traveler_ref
        Booking Traveler associated to this policy information.
    """

    class Meta:
        name = "PolicyInformation"
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    air_policy: list[TypeSegmentPolicy] = field(
        default_factory=list,
        metadata={
            "name": "AirPolicy",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    rail_policy: list[TypeSegmentPolicy] = field(
        default_factory=list,
        metadata={
            "name": "RailPolicy",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    hotel_policy: list[TypeSegmentPolicy] = field(
        default_factory=list,
        metadata={
            "name": "HotelPolicy",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    vehicle_policy: list[TypeSegmentPolicy] = field(
        default_factory=list,
        metadata={
            "name": "VehiclePolicy",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    booking_traveler_ref: str = field(
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "required": True,
        }
    )
