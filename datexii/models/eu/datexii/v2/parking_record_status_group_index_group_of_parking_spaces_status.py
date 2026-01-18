from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.group_of_parking_spaces_status import (
    GroupOfParkingSpacesStatus,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingRecordStatusGroupIndexGroupOfParkingSpacesStatus:
    class Meta:
        name = "_ParkingRecordStatusGroupIndexGroupOfParkingSpacesStatus"

    group_of_parking_spaces_status: GroupOfParkingSpacesStatus | None = (
        field(
            default=None,
            metadata={
                "name": "groupOfParkingSpacesStatus",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
                "required": True,
            },
        )
    )
    group_index: int | None = field(
        default=None,
        metadata={
            "name": "groupIndex",
            "type": "Attribute",
            "required": True,
        },
    )
