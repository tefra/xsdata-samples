from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class QueueNextModifiers:
    """
    Can only be used when modifying an Universal Record in Queue mode.If not
    specified along with ReturnRecord as false then current PNR in queue context
    will be removed.

    Parameters
    ----------
    next_on_queue
        Set to true to retrieve the next PNR on Queue ,if not set or set to
        false system would return the current PNR.NextOnQueue cannot be
        combined with Provider Locator Code and ReturnRecord as true
    provider_locator_code
        If providerLocatorCode is specified then system would return the
        specified locator code in Queue mode .Provider Locator Code cannot
        be combined with NextOnQueue and ReturnRecord as true
    re_queue_current
        Set to true to place the current PNR back on Queue
    queue_session_token
        Queue Session Token to hold session token for multiple queue
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    next_on_queue: None | bool = field(
        default=None,
        metadata={
            "name": "NextOnQueue",
            "type": "Attribute",
        },
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        },
    )
    re_queue_current: None | bool = field(
        default=None,
        metadata={
            "name": "ReQueueCurrent",
            "type": "Attribute",
        },
    )
    queue_session_token: None | str = field(
        default=None,
        metadata={
            "name": "QueueSessionToken",
            "type": "Attribute",
        },
    )
