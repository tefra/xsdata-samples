from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.fare_rule import FareRule

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AirFareRulesRsp(BaseRsp1):
    """
    Response to an AirFareRuleReq.

    Parameters
    ----------
    fare_rule
        Provider: 1G,1V,1P,ACH.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_rule: list[FareRule] = field(
        default_factory=list,
        metadata={
            "name": "FareRule",
            "type": "Element",
            "max_occurs": 999,
        },
    )
