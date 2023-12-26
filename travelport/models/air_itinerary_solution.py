from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_segment_ref import AirSegmentRef
from travelport.models.connection import Connection

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirItinerarySolution:
    """
    The pricing container for an air travel itinerary.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment_ref: list[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    connection: list[Connection] = field(
        default_factory=list,
        metadata={
            "name": "Connection",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
