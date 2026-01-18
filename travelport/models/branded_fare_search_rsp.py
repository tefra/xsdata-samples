from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.fare_family import FareFamily

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class BrandedFareSearchRsp(BaseRsp1):
    """
    Branded Fare search response.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    fare_family: list[FareFamily] = field(
        default_factory=list,
        metadata={
            "name": "FareFamily",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    more_results: bool = field(
        metadata={
            "name": "MoreResults",
            "type": "Attribute",
            "required": True,
        }
    )
