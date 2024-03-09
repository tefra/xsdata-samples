from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_2 import BaseReq2
from travelport.models.next_result_reference_2 import NextResultReference2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


@dataclass
class BaseSearchReq2(BaseReq2):
    class Meta:
        name = "BaseSearchReq"

    next_result_reference: list[NextResultReference2] = field(
        default_factory=list,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
        },
    )
