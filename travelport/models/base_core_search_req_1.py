from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_core_req_1 import BaseCoreReq1
from travelport.models.next_result_reference_1 import NextResultReference1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class BaseCoreSearchReq1(BaseCoreReq1):
    """
    Base Request for Air Search.
    """

    class Meta:
        name = "BaseCoreSearchReq"

    next_result_reference: list[NextResultReference1] = field(
        default_factory=list,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
