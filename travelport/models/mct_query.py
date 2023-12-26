from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_segment import AirSegment

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class MctQuery:
    """
    Lookup the particular MCT time between two segments.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_segment: list[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
