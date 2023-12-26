from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.next_result_reference_1 import NextResultReference1
from travelport.models.queue_selector_type import QueueSelectorType

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class GdsQueueListReq(BaseReq1):
    """
    Use this request to list the pnrs on a queue.

    Parameters
    ----------
    next_result_reference
        Container to send reference to additional queue list results
        (Providers: 1P) Error returned, "NextResultReference is not
        supported by the Provider." (Providers: 1V, 1G)
    gds_queue_selector
    provider_code
        The IATA assigned airline/GDS code.
    pseudo_city_code
    retrieve_all
        Set to true to retrieve all PNRs ,if not set or set to false system
        would display PNRs as returned from GDS .
    queue_session_token
        Queue Session Token to hold session token for multiple queue
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    next_result_reference: None | NextResultReference1 = field(
        default=None,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    gds_queue_selector: None | QueueSelectorType = field(
        default=None,
        metadata={
            "name": "GdsQueueSelector",
            "type": "Element",
            "required": True,
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
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        },
    )
    retrieve_all: None | bool = field(
        default=None,
        metadata={
            "name": "RetrieveAll",
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
