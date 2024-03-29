from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.booking_base_req import BookingBaseReq
from travelport.models.command import Command

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingTerminalReq(BookingBaseReq):
    """
    Allow terminal commands to be run in the session.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    command: None | Command = field(
        default=None,
        metadata={
            "name": "Command",
            "type": "Element",
            "required": True,
        },
    )
