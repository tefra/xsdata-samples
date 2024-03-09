from dataclasses import dataclass, field
from typing import Any

from .vehicle_stopping_position_version_structure import (
    VehicleStoppingPositionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleStoppingPosition(VehicleStoppingPositionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    members: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    url: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    image: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    postal_address: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    road_address: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
