from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.universal_record_search_result import (
    UniversalRecordSearchResult,
)

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class UniversalRecordSearchRsp(BaseRsp1):
    """
    Response containing summary information for reservations under a Universal
    Record.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record_search_result: list[UniversalRecordSearchResult] = field(
        default_factory=list,
        metadata={
            "name": "UniversalRecordSearchResult",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    more_results: None | bool = field(
        default=None,
        metadata={
            "name": "MoreResults",
            "type": "Attribute",
            "required": True,
        },
    )
