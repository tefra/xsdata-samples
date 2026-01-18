from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .vehicle_entrance_version_structure import VehicleEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleEntrance(VehicleEntranceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    members: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
