from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_6 import BaseRsp6
from travelport.models.next_result_reference_6 import NextResultReference6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class BaseSearchRsp6(BaseRsp6):
    class Meta:
        name = "BaseSearchRsp"

    next_result_reference: list[NextResultReference6] = field(
        default_factory=list,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
            "max_occurs": 999,
        }
    )
