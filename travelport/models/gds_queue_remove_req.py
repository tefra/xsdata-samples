from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.queue_selector_1 import QueueSelector1

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class GdsQueueRemoveReq(BaseReq1):
    """
    Use this request to Clear a GDS queue.

    Parameters
    ----------
    queue_selector
    queue_session_token
        Host session Token
    pseudo_city_code
    provider_code
    provider_locator_code
        ProviderLocatorCode of the PNR to be removed from the Queue
    remove_duplicates
        Remove duplicate PNRs from queues. Provider Supported 1P
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    queue_selector: None | QueueSelector1 = field(
        default=None,
        metadata={
            "name": "QueueSelector",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    queue_session_token: None | str = field(
        default=None,
        metadata={
            "name": "QueueSessionToken",
            "type": "Attribute",
        },
    )
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        },
    )
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
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        },
    )
    remove_duplicates: None | bool = field(
        default=None,
        metadata={
            "name": "RemoveDuplicates",
            "type": "Attribute",
        },
    )
