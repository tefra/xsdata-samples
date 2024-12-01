from dataclasses import dataclass, field
from typing import Any

from .stop_place_vehicle_entrance_version_structure import (
    StopPlaceVehicleEntranceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlaceVehicleEntrance(StopPlaceVehicleEntranceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    members: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
