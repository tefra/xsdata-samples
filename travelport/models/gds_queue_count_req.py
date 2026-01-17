from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.queue_pseudo_city_selector import (
    QueuePseudoCitySelector,
)

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class GdsQueueCountReq(BaseReq1):
    """
    Use this request to get the number of pnrs on a queue.

    If no queue is given, all queues for the pcc will be returned If no
    pseudocitycode is.

    Parameters
    ----------
    queue_pseudo_city_selector
    provider_code
        The IATA assigned airline/GDS code.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    queue_pseudo_city_selector: list[QueuePseudoCitySelector] = field(
        default_factory=list,
        metadata={
            "name": "QueuePseudoCitySelector",
            "type": "Element",
            "max_occurs": 999,
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
