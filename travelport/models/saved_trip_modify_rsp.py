from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.saved_trip import SavedTrip

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class SavedTripModifyRsp(BaseRsp1):
    """Response to SavedTripModifyReq.

    Contains the SavedTrip successfully modified.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    saved_trip: None | SavedTrip = field(
        default=None,
        metadata={
            "name": "SavedTrip",
            "type": "Element",
        },
    )
