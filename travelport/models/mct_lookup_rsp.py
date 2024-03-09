from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.mct_exception import MctException
from travelport.models.mct_standard import MctStandard

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class MctLookupRsp(BaseRsp1):
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    mct_standard: list[MctStandard] = field(
        default_factory=list,
        metadata={
            "name": "MctStandard",
            "type": "Element",
            "max_occurs": 4,
        },
    )
    mct_exception: list[MctException] = field(
        default_factory=list,
        metadata={
            "name": "MctException",
            "type": "Element",
            "max_occurs": 999,
        },
    )
