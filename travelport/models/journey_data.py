from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_segment import AirSegment

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class JourneyData:
    """
    Performs journey aware air availability.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment: list[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
        },
    )
