from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.booking_base_req import BookingBaseReq

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingRetrieveDocumentReq(BookingBaseReq):
    """
    Used view Ticket Details of the PNR.

    Parameters
    ----------
    air_reservation_locator_code
        Provider: 1G,1V,1P.
    ticket_number
        Provider: 1G,1V,1P.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    air_reservation_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_length": 5,
            "max_length": 8,
        }
    )
    ticket_number: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
            "min_length": 1,
            "max_length": 13,
        }
    )
