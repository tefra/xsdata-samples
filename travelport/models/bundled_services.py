from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.bundled_service import BundledService

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BundledServices:
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    bundled_service: list[BundledService] = field(
        default_factory=list,
        metadata={
            "name": "BundledService",
            "type": "Element",
            "max_occurs": 16,
        },
    )
