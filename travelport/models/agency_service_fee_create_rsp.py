from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.service_fee_info_1 import ServiceFeeInfo1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class AgencyServiceFeeCreateRsp(BaseRsp1):
    """
    Agency Service Fee issued through BSP or Airline Reporting Corporation
    (ARC)..
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    service_fee_info: list[ServiceFeeInfo1] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeeInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
