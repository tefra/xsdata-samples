from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.saved_trip_search_result import SavedTripSearchResult

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class SavedTripSearchRsp(BaseRsp1):
    """
    Response containing summary information of savedTrip.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    saved_trip_search_result: list[SavedTripSearchResult] = field(
        default_factory=list,
        metadata={
            "name": "SavedTripSearchResult",
            "type": "Element",
            "max_occurs": 999,
        }
    )
