from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.general_remark_1 import GeneralRemark1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class McoVoidReq(BaseReq1):
    """
    Void an MCO (of any type).

    Parameters
    ----------
    general_remark
    number
        The number of the MCO to void
    return_mco
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    general_remark: list[GeneralRemark1] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    number: str = field(
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )
    return_mco: bool = field(
        default=False,
        metadata={
            "name": "ReturnMCO",
            "type": "Attribute",
        },
    )
