from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.search_ticketing_reservation_status_6 import SearchTicketingReservationStatus6
from travelport.models.search_ticketing_ticket_status_6 import SearchTicketingTicketStatus6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class SearchTicketing6:
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
        namespace = "http://www.travelport.com/schema/common_v38_0"

    ticket_status: SearchTicketingTicketStatus6 = field(
        default=SearchTicketingTicketStatus6.BOTH,
        metadata={
            "name": "TicketStatus",
            "type": "Attribute",
        }
    )
    reservation_status: SearchTicketingReservationStatus6 = field(
        default=SearchTicketingReservationStatus6.BOTH,
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
