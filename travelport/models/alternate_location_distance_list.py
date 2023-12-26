from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.alternate_location_distance import (
    AlternateLocationDistance,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AlternateLocationDistanceList:
    """
    Provides the Distance Information between Original Search Airports or City to
    Alternate Search Airports.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    alternate_location_distance: list[AlternateLocationDistance] = field(
        default_factory=list,
        metadata={
            "name": "AlternateLocationDistance",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
