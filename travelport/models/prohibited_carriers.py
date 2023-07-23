from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.carrier_1 import Carrier1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class ProhibitedCarriers:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    carrier: list[Carrier1] = field(
        default_factory=list,
        metadata={
            "name": "Carrier",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
