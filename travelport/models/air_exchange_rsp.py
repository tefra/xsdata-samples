from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.booking_traveler_1 import BookingTraveler1
from travelport.models.ticket_number_1 import TicketNumber1
from travelport.models.type_air_reservation_with_fop import (
    TypeAirReservationWithFop,
)
from travelport.models.type_ticket_failure_info import TypeTicketFailureInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirExchangeRsp(BaseRsp1):
    """
    Parameters
    ----------
    ticket_number
    booking_traveler
        Provider: ACH.
    air_reservation
        Provider: ACH.
    exchange_failure_info
        Provider: ACH.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    ticket_number: list[TicketNumber1] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    booking_traveler: list[BookingTraveler1] = field(
        default_factory=list,
        metadata={
            "name": "BookingTraveler",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    air_reservation: None | TypeAirReservationWithFop = field(
        default=None,
        metadata={
            "name": "AirReservation",
            "type": "Element",
        },
    )
    exchange_failure_info: list[TypeTicketFailureInfo] = field(
        default_factory=list,
        metadata={
            "name": "ExchangeFailureInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
