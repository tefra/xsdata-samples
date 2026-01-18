from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_3 import BaseRsp3
from travelport.models.next_result_reference_3 import NextResultReference3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class BaseSearchRsp3(BaseRsp3):
    class Meta:
        name = "BaseSearchRsp"

    next_result_reference: list[NextResultReference3] = field(
        default_factory=list,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
            "max_occurs": 999,
        },
    )
