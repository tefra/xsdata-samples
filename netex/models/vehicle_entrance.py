from dataclasses import dataclass, field
from typing import Any

from .vehicle_entrance_version_structure import VehicleEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleEntrance(VehicleEntranceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    members: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
