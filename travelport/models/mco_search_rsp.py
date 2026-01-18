from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.mco_search_result import McoSearchResult

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class McoSearchRsp(BaseRsp1):
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    mco_search_result: list[McoSearchResult] = field(
        default_factory=list,
        metadata={
            "name": "McoSearchResult",
            "type": "Element",
            "max_occurs": 999,
        },
    )
