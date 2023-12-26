from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_associated_remark_3 import TypeAssociatedRemark3
from travelport.models.type_non_air_reservation_ref_4 import (
    TypeNonAirReservationRef4,
)
from travelport.models.type_segment_ref_4 import TypeSegmentRef4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class InvoiceRemark3(TypeAssociatedRemark3):
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
        namespace = "http://www.travelport.com/schema/common_v33_0"

    air_segment_ref: None | TypeSegmentRef4 = field(
        default=None,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
        },
    )
    hotel_reservation_ref: None | TypeNonAirReservationRef4 = field(
        default=None,
        metadata={
            "name": "HotelReservationRef",
            "type": "Element",
        },
    )
    vehicle_reservation_ref: None | TypeNonAirReservationRef4 = field(
        default=None,
        metadata={
            "name": "VehicleReservationRef",
            "type": "Element",
        },
    )
    passive_segment_ref: None | TypeSegmentRef4 = field(
        default=None,
        metadata={
            "name": "PassiveSegmentRef",
            "type": "Element",
        },
    )
