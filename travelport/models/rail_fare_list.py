from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.rail_fare import RailFare

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailFareList:
    """
    The shared object list of FareInfos.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_fare: list[RailFare] = field(
        default_factory=list,
        metadata={
            "name": "RailFare",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
