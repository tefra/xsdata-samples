from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_non_air_reservation_ref_2 import (
    TypeNonAirReservationRef2,
)
from travelport.models.type_segment_ref_2 import TypeSegmentRef2

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class SegmentSelect:
    """
    To be used to pass the selected segment.

    Parameters
    ----------
    air_segment_ref
        Reference to AirSegment from an Air Reservation.
    hotel_reservation_ref
        Specify the locator code of Hotel reservation if it needs to be
        considered as Auxiliary segment
    vehicle_reservation_ref
        Specify the locator code of Vehicle reservation if it needs to be
        considered as Auxiliary segment
    passive_segment_ref
        Reference to PassiveSegment from a Passive Reservation.Specify the
        passive segment if it needs to be considered as Auxiliary segment
    all_confirmed_air
        Set to true to consider all Confirmed segments including active and
        passive and set to false to discard confirmed segments
    all_waitlisted_air
        Set to true to consider all Waitlisted segments and false to discard
        all waitlisted segments
    all_hotel
        Set to true to consider all Hotel reservations as Auxiliary segment
        and false to discard all Hotel reservations
    all_vehicle
        Set to true to consider all Vehicle reservations as Auxiliary
        segment and false to discard all Vehicle reservations
    all_passive
        Set to true to consider all Passive segments as Auxiliary segment
        and false to discard passive segments
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment_ref: list[TypeSegmentRef2] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    hotel_reservation_ref: list[TypeNonAirReservationRef2] = field(
        default_factory=list,
        metadata={
            "name": "HotelReservationRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    vehicle_reservation_ref: list[TypeNonAirReservationRef2] = field(
        default_factory=list,
        metadata={
            "name": "VehicleReservationRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    passive_segment_ref: list[TypeSegmentRef2] = field(
        default_factory=list,
        metadata={
            "name": "PassiveSegmentRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    all_confirmed_air: None | bool = field(
        default=None,
        metadata={
            "name": "AllConfirmedAir",
            "type": "Attribute",
        },
    )
    all_waitlisted_air: None | bool = field(
        default=None,
        metadata={
            "name": "AllWaitlistedAir",
            "type": "Attribute",
        },
    )
    all_hotel: None | bool = field(
        default=None,
        metadata={
            "name": "AllHotel",
            "type": "Attribute",
        },
    )
    all_vehicle: None | bool = field(
        default=None,
        metadata={
            "name": "AllVehicle",
            "type": "Attribute",
        },
    )
    all_passive: None | bool = field(
        default=None,
        metadata={
            "name": "AllPassive",
            "type": "Attribute",
        },
    )
