from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.mco_1 import Mco1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class CreateAirlineFeeMcoRsp(BaseRsp1):
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    mco: None | Mco1 = field(
        default=None,
        metadata={
            "name": "MCO",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        },
    )
