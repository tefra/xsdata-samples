from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.parking_space_basics import (
    ParkingSpaceBasics,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class ParkingSpace2:
    class Meta:
        name = "_ParkingSpace"

    parking_space_basics: ParkingSpaceBasics = field(
        metadata={
            "name": "parkingSpaceBasics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_space_index: int = field(
        metadata={
            "name": "parkingSpaceIndex",
            "type": "Attribute",
            "required": True,
        }
    )
