from __future__ import annotations

from dataclasses import dataclass, field

from .all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from .submode_ref_structure import SubmodeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ModeRefStructure(SubmodeRefStructure):
    mode: AllVehicleModesOfTransportEnumeration = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
