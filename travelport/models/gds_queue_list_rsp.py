from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.next_result_reference_1 import NextResultReference1
from travelport.models.queue_element import QueueElement

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass(kw_only=True)
class GdsQueueListRsp(BaseRsp1):
    """
    The response from the host for a queue list.

    Parameters
    ----------
    next_result_reference
        Container to return reference to additional queue list results
        (Providers: 1P)
    queue_element
    more_pnrexists
        This is an indicator which indicates there are more PNRs in queue
        than what is returned. If true means more PNRs exist in the Queue.
        If false or not present means all PNRs are already returned in
        response from the queue.
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
    queue_element: list[QueueElement] = field(
        default_factory=list,
        metadata={
            "name": "QueueElement",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    more_pnrexists: None | bool = field(
        default=None,
        metadata={
            "name": "MorePNRExists",
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
