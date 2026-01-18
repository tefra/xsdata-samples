from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.parking_space_basics import (
    ParkingSpaceBasics,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class GroupOfParkingSpaces2:
    class Meta:
        name = "_GroupOfParkingSpaces"

    parking_space_basics: ParkingSpaceBasics | None = field(
        default=None,
        metadata={
            "name": "parkingSpaceBasics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    group_index: int | None = field(
        default=None,
        metadata={
            "name": "groupIndex",
            "type": "Attribute",
            "required": True,
        },
    )
