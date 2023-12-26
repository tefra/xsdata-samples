from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.credit_card_auth_1 import CreditCardAuth1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class CreditCardAuthRsp(BaseRsp1):
    """
    The response to the CreditCardAuthReq.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    credit_card_auth: list[CreditCardAuth1] = field(
        default_factory=list,
        metadata={
            "name": "CreditCardAuth",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
