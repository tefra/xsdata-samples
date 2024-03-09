from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailJourneyRef:
    """
    Reference to a RailJourney.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
