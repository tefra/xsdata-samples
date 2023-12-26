from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_core_req_3 import BaseCoreReq3
from travelport.models.next_result_reference_3 import NextResultReference3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class BaseCoreSearchReq3(BaseCoreReq3):
    """
    Base Request for Air Search.
    """

    class Meta:
        name = "BaseCoreSearchReq"

    next_result_reference: list[NextResultReference3] = field(
        default_factory=list,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
            "max_occurs": 999,
        },
    )
