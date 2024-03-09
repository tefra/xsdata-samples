from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingStartReq(BaseReq1):
    """
    Used to start session.

    Parameters
    ----------
    provider_code
        Provider with which session needs to be started.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        },
    )
