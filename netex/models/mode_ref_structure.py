from __future__ import annotations

from dataclasses import dataclass, field

from .all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from .submode_ref_structure import SubmodeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ModeRefStructure(SubmodeRefStructure):
    mode: AllVehicleModesOfTransportEnumeration | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
