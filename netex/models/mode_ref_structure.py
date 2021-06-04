from dataclasses import dataclass, field
from typing import Optional
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.submode_ref_structure import SubmodeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ModeRefStructure(SubmodeRefStructure):
    mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
