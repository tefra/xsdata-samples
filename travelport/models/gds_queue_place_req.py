from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.queue_selector_1 import QueueSelector1

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass(kw_only=True)
class GdsQueuePlaceReq(BaseReq1):
    """
    Use this request to place a UR on a queue.

    Parameters
    ----------
    queue_selector
        Identifies the Queue Information to be selected for placing the UR
        An UR can be placed into multiple Queues
    pseudo_city_code
        Input PCC optional value for placing the UR into Queue
    provider_code
    provider_locator_code
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    queue_selector: list[QueueSelector1] = field(
        default_factory=list,
        metadata={
            "name": "QueueSelector",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
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
    provider_code: str = field(
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_locator_code: str = field(
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )
