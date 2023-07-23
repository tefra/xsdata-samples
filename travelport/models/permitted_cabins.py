from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.cabin_class_1 import CabinClass1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PermittedCabins:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    cabin_class: list[CabinClass1] = field(
        default_factory=list,
        metadata={
            "name": "CabinClass",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )
