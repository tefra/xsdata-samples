from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.universal_record_history_search_result import (
    UniversalRecordHistorySearchResult,
)

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class UniversalRecordHistorySearchRsp(BaseRsp1):
    """
    Parameters
    ----------
    universal_record_history_search_result
    last_result
        Indicate when the search query reached the last result.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record_history_search_result: list[
        UniversalRecordHistorySearchResult
    ] = field(
        default_factory=list,
        metadata={
            "name": "UniversalRecordHistorySearchResult",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    last_result: None | bool = field(
        default=None,
        metadata={
            "name": "LastResult",
            "type": "Attribute",
        },
    )
