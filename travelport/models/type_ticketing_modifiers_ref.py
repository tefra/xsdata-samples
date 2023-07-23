from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_pricing_info_ref import AirPricingInfoRef

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TypeTicketingModifiersRef:
    class Meta:
        name = "typeTicketingModifiersRef"

    air_pricing_info_ref: list[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
