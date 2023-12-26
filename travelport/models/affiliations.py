from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.travel_arranger import TravelArranger

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Affiliations:
    """
    Affiliations related for pre pay profiles.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    travel_arranger: list[TravelArranger] = field(
        default_factory=list,
        metadata={
            "name": "TravelArranger",
            "type": "Element",
            "max_occurs": 999,
        },
    )
