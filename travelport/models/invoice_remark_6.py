from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_associated_remark_6 import TypeAssociatedRemark6
from travelport.models.type_non_air_reservation_ref_7 import (
    TypeNonAirReservationRef7,
)
from travelport.models.type_segment_ref_7 import TypeSegmentRef7

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class InvoiceRemark6(TypeAssociatedRemark6):
    """
    Parameters
    ----------
    air_segment_ref
        Reference to AirSegment from an Air Reservation.
    hotel_reservation_ref
        Specify the locator code of Hotel reservation.
    vehicle_reservation_ref
        Specify the locator code of Vehicle reservation.
    passive_segment_ref
        Reference to PassiveSegment from a Passive Reservation.
    """

    class Meta:
        name = "InvoiceRemark"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    air_segment_ref: None | TypeSegmentRef7 = field(
        default=None,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
        },
    )
    hotel_reservation_ref: None | TypeNonAirReservationRef7 = field(
        default=None,
        metadata={
            "name": "HotelReservationRef",
            "type": "Element",
        },
    )
    vehicle_reservation_ref: None | TypeNonAirReservationRef7 = field(
        default=None,
        metadata={
            "name": "VehicleReservationRef",
            "type": "Element",
        },
    )
    passive_segment_ref: None | TypeSegmentRef7 = field(
        default=None,
        metadata={
            "name": "PassiveSegmentRef",
            "type": "Element",
        },
    )
