from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.mct_count import MctCount

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class MctCountRsp(BaseRsp1):
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    mct_count: list[MctCount] = field(
        default_factory=list,
        metadata={
            "name": "MctCount",
            "type": "Element",
            "max_occurs": 999,
        }
    )
