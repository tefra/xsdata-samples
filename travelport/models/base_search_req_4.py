from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_4 import BaseReq4
from travelport.models.next_result_reference_4 import NextResultReference4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class BaseSearchReq4(BaseReq4):
    class Meta:
        name = "BaseSearchReq"

    next_result_reference: list[NextResultReference4] = field(
        default_factory=list,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "max_occurs": 999,
        },
    )
