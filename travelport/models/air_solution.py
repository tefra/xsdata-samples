from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_segment import AirSegment
from travelport.models.fare_basis import FareBasis
from travelport.models.host_token_1 import HostToken1
from travelport.models.search_traveler import SearchTraveler

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AirSolution:
    """
    Defines an air solution that is comprised of an itinerary (the
    segments) along with the passengers.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    search_traveler: list[SearchTraveler] = field(
        default_factory=list,
        metadata={
            "name": "SearchTraveler",
            "type": "Element",
            "max_occurs": 9,
        },
    )
    air_segment: list[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 16,
        },
    )
    host_token: list[HostToken1] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 16,
        },
    )
    fare_basis: list[FareBasis] = field(
        default_factory=list,
        metadata={
            "name": "FareBasis",
            "type": "Element",
            "max_occurs": 16,
        },
    )
