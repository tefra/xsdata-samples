from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.brand import Brand

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BrandList:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    brand: list[Brand] = field(
        default_factory=list,
        metadata={
            "name": "Brand",
            "type": "Element",
            "max_occurs": 99,
        }
    )
