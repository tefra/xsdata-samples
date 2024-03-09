from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.rail_journey import RailJourney

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailJourneyList:
    """
    List of Rail Journeys.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_journey: list[RailJourney] = field(
        default_factory=list,
        metadata={
            "name": "RailJourney",
            "type": "Element",
            "max_occurs": 999,
        },
    )
