from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.universal_record import UniversalRecord

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class GdsNextOnQueueRsp(BaseRsp1):
    """
    The response from the host for a NextOnQueueReq.

    Parameters
    ----------
    universal_record
        Refers to the Universal Record , system would automatically import a
        PNR if it doesn't exist exist in the sytem otherwise would display
        existing Universal Record.
    queue_session_token
        Queue Session Token to hold session token for multiple queue
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    universal_record: None | UniversalRecord = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/universal_v52_0",
        },
    )
    queue_session_token: None | str = field(
        default=None,
        metadata={
            "name": "QueueSessionToken",
            "type": "Attribute",
        },
    )
