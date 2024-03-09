from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.parking_space_1 import ParkingSpace1

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class GroupOfParkingSpacesParkingSpaceIndexParkingSpace:
    class Meta:
        name = "_GroupOfParkingSpacesParkingSpaceIndexParkingSpace"

    parking_space: Optional[ParkingSpace1] = field(
        default=None,
        metadata={
            "name": "parkingSpace",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    parking_space_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkingSpaceIndex",
            "type": "Attribute",
            "required": True,
        },
    )
