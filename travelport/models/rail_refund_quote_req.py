from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailRefundQuoteReq(BaseReq1):
    """
    Request to quote a refund for an itinerary.

    Parameters
    ----------
    locator_code
        The unique identifier for this rail reservation
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    locator_code: None | str = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        },
    )
