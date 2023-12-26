from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_core_req_4 import BaseCoreReq4
from travelport.models.next_result_reference_4 import NextResultReference4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class BaseCoreSearchReq4(BaseCoreReq4):
    """
    Base Request for Air Search.
    """

    class Meta:
        name = "BaseCoreSearchReq"

    next_result_reference: list[NextResultReference4] = field(
        default_factory=list,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "max_occurs": 999,
        },
    )
