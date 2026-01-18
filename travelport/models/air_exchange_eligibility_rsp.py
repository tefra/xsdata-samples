from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.exchange_eligibility_info import ExchangeEligibilityInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AirExchangeEligibilityRsp(BaseRsp1):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    exchange_eligibility_info: ExchangeEligibilityInfo = field(
        metadata={
            "name": "ExchangeEligibilityInfo",
            "type": "Element",
            "required": True,
        }
    )
