from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_5 import BaseReq5
from travelport.models.next_result_reference_5 import NextResultReference5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class BaseSearchReq5(BaseReq5):
    class Meta:
        name = "BaseSearchReq"

    next_result_reference: list[NextResultReference5] = field(
        default_factory=list,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "max_occurs": 999,
        },
    )
