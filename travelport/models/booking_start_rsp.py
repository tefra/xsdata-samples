from __future__ import annotations
from dataclasses import dataclass
from travelport.models.booking_base_rsp import BookingBaseRsp

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingStartRsp(BookingBaseRsp):
    """Returns the session key.

    User must use the session key in the subsequent transactions to use
    the created session.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"
