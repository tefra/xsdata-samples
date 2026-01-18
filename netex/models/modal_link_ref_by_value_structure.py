from __future__ import annotations

from dataclasses import dataclass, field

from .link_ref_by_value_structure import LinkRefByValueStructure
from .vehicle_mode import VehicleMode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ModalLinkRefByValueStructure(LinkRefByValueStructure):
    vehicle_mode: None | VehicleMode = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
