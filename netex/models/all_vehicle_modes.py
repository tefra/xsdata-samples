from __future__ import annotations

from dataclasses import dataclass, field

from .all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AllVehicleModes:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AllVehicleModesOfTransportEnumeration | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
