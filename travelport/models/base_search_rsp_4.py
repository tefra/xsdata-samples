from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_4 import BaseRsp4
from travelport.models.next_result_reference_4 import NextResultReference4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class BaseSearchRsp4(BaseRsp4):
    class Meta:
        name = "BaseSearchRsp"

    next_result_reference: list[NextResultReference4] = field(
        default_factory=list,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "max_occurs": 999,
        }
    )
