from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.parking_space_basics import ParkingSpaceBasics

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingSpace2:
    class Meta:
        name = "_ParkingSpace"

    parking_space_basics: Optional[ParkingSpaceBasics] = field(
        default=None,
        metadata={
            "name": "parkingSpaceBasics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_space_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkingSpaceIndex",
            "type": "Attribute",
            "required": True,
        }
    )
