from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_segment import AirSegment
from travelport.models.host_token_1 import HostToken1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class AddAirSegment:
    """
    Container for Air Segment to be added.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    air_segment: list[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 8,
        },
    )
    host_token: list[HostToken1] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 8,
        },
    )
