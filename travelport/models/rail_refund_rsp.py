from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.mco_1 import Mco1
from travelport.models.payment_1 import Payment1

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailRefundRsp(BaseRsp1):
    """
    Returns rail cancel information.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    payment: None | Payment1 = field(
        default=None,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    mco: None | Mco1 = field(
        default=None,
        metadata={
            "name": "MCO",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
