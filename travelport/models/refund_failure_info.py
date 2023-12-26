from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.name_1 import Name1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class RefundFailureInfo:
    """
    Will be optionally returned as part of AirRefunTicketingRsp if one or all
    ticket refund requests fail.

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
        namespace = "http://www.travelport.com/schema/air_v52_0"

    ticket_number: None | str = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_length": 1,
            "max_length": 13,
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
        },
    )
    booking_traveler_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
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
