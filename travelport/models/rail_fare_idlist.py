from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.rail_fare_id import RailFareId

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailFareIdlist:
    """
    The shared object list of FareIDs.
    """

    class Meta:
        name = "RailFareIDList"
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_fare_id: list[RailFareId] = field(
        default_factory=list,
        metadata={
            "name": "RailFareID",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
