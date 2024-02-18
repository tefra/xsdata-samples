from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.name_1 import Name1
from travelport.models.ticket_number_1 import TicketNumber1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TypeTicketFailureInfo:
    """
    Will be optionally returned as part if one or all ticketing requests fail.

    Parameters
    ----------
    ticket_number
    name
    tcrnumber
        The identifying number for a Ticketless Air Reservation.
    booking_traveler_ref
    code
    message
    """

    class Meta:
        name = "typeTicketFailureInfo"

    ticket_number: None | TicketNumber1 = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    name: None | Name1 = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    tcrnumber: None | str = field(
        default=None,
        metadata={
            "name": "TCRNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    booking_traveler_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    code: None | int = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        },
    )
    message: None | str = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Attribute",
        },
    )
