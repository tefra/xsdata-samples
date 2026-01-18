from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.mct_search import MctSearch

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class MctCountReq(BaseReq1):
    """
    Determine how many MCT exceptions exist for the search criteria.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    mct_search: MctSearch = field(
        metadata={
            "name": "MctSearch",
            "type": "Element",
            "required": True,
        }
    )
