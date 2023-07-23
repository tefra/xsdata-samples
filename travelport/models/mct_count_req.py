from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.mct_search import MctSearch

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class MctCountReq(BaseReq1):
    """
    Determine how many MCT exceptions exist for the search criteria.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    mct_search: None | MctSearch = field(
        default=None,
        metadata={
            "name": "MctSearch",
            "type": "Element",
            "required": True,
        }
    )
