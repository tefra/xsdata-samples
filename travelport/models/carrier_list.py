from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.carrier_code import CarrierCode

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class CarrierList:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    carrier_code: list[CarrierCode] = field(
        default_factory=list,
        metadata={
            "name": "CarrierCode",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 6,
        },
    )
    include_carrier: None | bool = field(
        default=None,
        metadata={
            "name": "IncludeCarrier",
            "type": "Attribute",
            "required": True,
        },
    )
