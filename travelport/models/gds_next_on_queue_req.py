from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.queue_pseudo_city_selector import (
    QueuePseudoCitySelector,
)

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass(kw_only=True)
class GdsNextOnQueueReq(BaseReq1):
    """
    Use this request to get the 'next' pnr on queue.

    Parameters
    ----------
    queue_pseudo_city_selector
        Target Queue where the current PNR needs to be placed. Supported
        Providers: Worldspan
    remove_current
        If specified and set to true, the pnr currently in context will be
        removed, if set to false then the current PNR will be placed back on
        the Queue.
    provider_locator_code
        If providerLocatorCode is not specified then the next PNR on the
        Queue will be retrieved.
    queue_session_token
        Queue Session Token to hold session token for multiple queue
    queue_continue
        Should be used only when the bottom of the queue has been reached.
        If set to true, will get the PNR from the top of the queue.
        Applicable Provider: Worldspan
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
    remove_current: bool = field(
        metadata={
            "name": "RemoveCurrent",
            "type": "Attribute",
            "required": True,
        }
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
    queue_session_token: None | str = field(
        default=None,
        metadata={
            "name": "QueueSessionToken",
            "type": "Attribute",
        },
    )
    queue_continue: None | bool = field(
        default=None,
        metadata={
            "name": "QueueContinue",
            "type": "Attribute",
        },
    )
    provider_code: str = field(
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
