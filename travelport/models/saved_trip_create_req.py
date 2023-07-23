from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.saved_trip import SavedTrip

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class SavedTripCreateReq(BaseReq1):
    """
    Request to create a SavedTrip.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    saved_trip: None | SavedTrip = field(
        default=None,
        metadata={
            "name": "SavedTrip",
            "type": "Element",
        }
    )
