from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_pricing_info import AirPricingInfo
from travelport.models.auto_pricing_info import AutoPricingInfo

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass(kw_only=True)
class AddPricing:
    """
    Container for Pricing to be added.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    air_pricing_info: list[AirPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 100,
        },
    )
    auto_pricing_info: list[AutoPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "AutoPricingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 100,
        },
    )
