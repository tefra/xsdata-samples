from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_core_req_2 import BaseCoreReq2
from travelport.models.next_result_reference_2 import NextResultReference2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


@dataclass(kw_only=True)
class BaseCoreSearchReq2(BaseCoreReq2):
    """
    Base Request for Air Search.
    """

    class Meta:
        name = "BaseCoreSearchReq"

    next_result_reference: list[NextResultReference2] = field(
        default_factory=list,
        metadata={
            "name": "NextResultReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
        },
    )
