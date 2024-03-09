from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PassengerTicketNumber:
    """
    Information related to Ticket Number.

    Parameters
    ----------
    ticket_number
        The identifying number for a Ticket for a passenger.
    booking_traveler_ref
        Reference to a passenger associated with a ticket.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    ticket_number: None | str = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 13,
        },
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        },
    )
