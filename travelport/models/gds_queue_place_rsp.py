from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.universal_record import UniversalRecord

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class GdsQueuePlaceRsp(BaseRsp1):
    """
    An empty response indicates success.

    Parameters
    ----------
    universal_record
        The Queue Place Response will return the UR Record
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
