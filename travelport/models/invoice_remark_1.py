from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_associated_remark_1 import TypeAssociatedRemark1
from travelport.models.type_non_air_reservation_ref_1 import (
    TypeNonAirReservationRef1,
)
from travelport.models.type_segment_ref_1 import TypeSegmentRef1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class InvoiceRemark1(TypeAssociatedRemark1):
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
        namespace = "http://www.travelport.com/schema/common_v52_0"

    air_segment_ref: None | TypeSegmentRef1 = field(
        default=None,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
        },
    )
    hotel_reservation_ref: None | TypeNonAirReservationRef1 = field(
        default=None,
        metadata={
            "name": "HotelReservationRef",
            "type": "Element",
        },
    )
    vehicle_reservation_ref: None | TypeNonAirReservationRef1 = field(
        default=None,
        metadata={
            "name": "VehicleReservationRef",
            "type": "Element",
        },
    )
    passive_segment_ref: None | TypeSegmentRef1 = field(
        default=None,
        metadata={
            "name": "PassiveSegmentRef",
            "type": "Element",
        },
    )
