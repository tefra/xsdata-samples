from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_segment import AirSegment
from travelport.models.apisrequirements import Apisrequirements
from travelport.models.host_token_1 import HostToken1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirItinerary:
    """
    A container for an Air only travel itinerary.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment: list[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    host_token: list[HostToken1] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    apisrequirements: list[Apisrequirements] = field(
        default_factory=list,
        metadata={
            "name": "APISRequirements",
            "type": "Element",
            "max_occurs": 999,
        },
    )
