from __future__ import annotations

from dataclasses import dataclass, field

from .all_modes_enumeration import AllModesEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadVehicleMode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AllModesEnumeration = field(
        metadata={
            "required": True,
        }
    )
