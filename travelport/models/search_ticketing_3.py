from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.search_ticketing_reservation_status_3 import SearchTicketingReservationStatus3
from travelport.models.search_ticketing_ticket_status_3 import SearchTicketingTicketStatus3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class SearchTicketing3:
    """
    Search restriction by Agent.

    Parameters
    ----------
    ticket_status
        Return only PNRs with ticketed, non-ticketed or both
    reservation_status
        Used only if "TicketStatus" set to "No" or "Both". Return only PNRs
        with specific reservation status or both statuses.
    ticket_date
        Identifies when this reservation was ticketed, or when it should be
        ticketed by (in the event of a TTL)
    """
    class Meta:
        name = "SearchTicketing"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    ticket_status: SearchTicketingTicketStatus3 = field(
        default=SearchTicketingTicketStatus3.BOTH,
        metadata={
            "name": "TicketStatus",
            "type": "Attribute",
        }
    )
    reservation_status: SearchTicketingReservationStatus3 = field(
        default=SearchTicketingReservationStatus3.BOTH,
        metadata={
            "name": "ReservationStatus",
            "type": "Attribute",
        }
    )
    ticket_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "TicketDate",
            "type": "Attribute",
        }
    )
