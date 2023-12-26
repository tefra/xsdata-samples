from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.parking_space_status import (
    ParkingSpaceStatus,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingRecordStatusParkingSpaceIndexParkingSpaceStatus:
    class Meta:
        name = "_ParkingRecordStatusParkingSpaceIndexParkingSpaceStatus"

    parking_space_status: Optional[ParkingSpaceStatus] = field(
        default=None,
        metadata={
            "name": "parkingSpaceStatus",
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
