from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_associated_remark_5 import TypeAssociatedRemark5
from travelport.models.type_non_air_reservation_ref_6 import (
    TypeNonAirReservationRef6,
)
from travelport.models.type_segment_ref_6 import TypeSegmentRef6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class InvoiceRemark5(TypeAssociatedRemark5):
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
        namespace = "http://www.travelport.com/schema/common_v34_0"

    air_segment_ref: None | TypeSegmentRef6 = field(
        default=None,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
        },
    )
    hotel_reservation_ref: None | TypeNonAirReservationRef6 = field(
        default=None,
        metadata={
            "name": "HotelReservationRef",
            "type": "Element",
        },
    )
    vehicle_reservation_ref: None | TypeNonAirReservationRef6 = field(
        default=None,
        metadata={
            "name": "VehicleReservationRef",
            "type": "Element",
        },
    )
    passive_segment_ref: None | TypeSegmentRef6 = field(
        default=None,
        metadata={
            "name": "PassiveSegmentRef",
            "type": "Element",
        },
    )
