from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.queue_pseudo_city_selector import (
    QueuePseudoCitySelector,
)

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class GdsExitQueueReq(BaseReq1):
    """
    Use this request to close a session you no longer need.

    Parameters
    ----------
    queue_pseudo_city_selector
        Target Queue where the current PNR needs to be placed. Supported
        Providers: Worldspan
    remove_current
        If specified and set to true, the pnr currently in context will be
        removed, if set to false then the current PNR will be placed back on
        the Queue.
    queue_session_token
        Queue Session Token to hold session token for multiple queue
    provider_code
        The IATA assigned airline/GDS code.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    queue_pseudo_city_selector: None | QueuePseudoCitySelector = field(
        default=None,
        metadata={
            "name": "QueuePseudoCitySelector",
            "type": "Element",
        },
    )
    remove_current: None | bool = field(
        default=None,
        metadata={
            "name": "RemoveCurrent",
            "type": "Attribute",
            "required": True,
        },
    )
    queue_session_token: None | str = field(
        default=None,
        metadata={
            "name": "QueueSessionToken",
            "type": "Attribute",
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
