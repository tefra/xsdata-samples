from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_pricing_info import AirPricingInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirPricingInfoList:
    """
    The shared object list of AirSegments.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_pricing_info: list[AirPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
