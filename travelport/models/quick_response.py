from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class QuickResponse:
    """
    Parameters
    ----------
    fast_result
        Set to true on initial request to have results returned immediately
        and may contain fewer hotels. Default is false.
    more_token
        Token is returned for use in subsequent request to retrieve complete
        results.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    fast_result: None | bool = field(
        default=None,
        metadata={
            "name": "FastResult",
            "type": "Attribute",
        }
    )
    more_token: None | str = field(
        default=None,
        metadata={
            "name": "MoreToken",
            "type": "Attribute",
        }
    )
