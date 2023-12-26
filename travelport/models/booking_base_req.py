from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingBaseReq(BaseReq1):
    """
    Context for Requests.

    Parameters
    ----------
    session_key
        System generated session token. Token contains the session
        information of the user. User must supply this in the resquest to
        use the current session they are working on.
    """

    session_key: None | str = field(
        default=None,
        metadata={
            "name": "SessionKey",
            "type": "Attribute",
        },
    )
