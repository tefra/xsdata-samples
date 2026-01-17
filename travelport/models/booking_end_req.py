from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.booking_base_req import BookingBaseReq
from travelport.models.booking_end_req_session_activity import (
    BookingEndReqSessionActivity,
)
from travelport.models.queue_selector_1 import QueueSelector1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingEndReq(BookingBaseReq):
    """
    Ends the session.

    Will end transact the booking on the host and create a UR, or will
    ignore the current activity.

    Parameters
    ----------
    session_activity
        Current values supported are  Ignore, End and EndQueue (QueueNumber
        must follow)
    queue_selector
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    session_activity: None | BookingEndReqSessionActivity = field(
        default=None,
        metadata={
            "name": "SessionActivity",
            "type": "Element",
            "required": True,
        },
    )
    queue_selector: list[QueueSelector1] = field(
        default_factory=list,
        metadata={
            "name": "QueueSelector",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 4,
        },
    )
