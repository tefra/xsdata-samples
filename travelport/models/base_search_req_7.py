from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_7 import BaseReq7
from travelport.models.next_result_reference_7 import NextResultReference7

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class BaseSearchReq7(BaseReq7):
    class Meta:
        name = "BaseSearchReq"

    next_result_reference: list[NextResultReference7] = field(
        default_factory=list,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
            "max_occurs": 999,
        },
    )
