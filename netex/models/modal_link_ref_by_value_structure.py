from dataclasses import dataclass, field
from typing import Optional
from .all_modes_enumeration import AllModesEnumeration
from .link_ref_by_value_structure import LinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ModalLinkRefByValueStructure(LinkRefByValueStructure):
    vehicle_mode: Optional[AllModesEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
