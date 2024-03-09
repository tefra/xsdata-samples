from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_pricing_solution import AirPricingSolution
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.fare_rule import FareRule

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirRepriceRsp(BaseRsp1):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_pricing_solution: None | AirPricingSolution = field(
        default=None,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "required": True,
        },
    )
    fare_rule: list[FareRule] = field(
        default_factory=list,
        metadata={
            "name": "FareRule",
            "type": "Element",
            "max_occurs": 999,
        },
    )
