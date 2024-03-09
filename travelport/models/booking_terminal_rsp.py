from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.booking_base_rsp import BookingBaseRsp
from travelport.models.command_response import CommandResponse

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingTerminalRsp(BookingBaseRsp):
    """
    Returns the terminal response and UR with the changes based on the Terminal
    Req.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    command_response: None | CommandResponse = field(
        default=None,
        metadata={
            "name": "CommandResponse",
            "type": "Element",
        },
    )
