from dataclasses import dataclass, field
from typing import Optional

from .all_modes_enumeration import AllModesEnumeration
from .place_ref_structure import PlaceRefStructure
from .point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessEndStructure:
    transport_mode: AllModesEnumeration | None = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    place_ref: PlaceRefStructure | None = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    point_ref: PointRefStructure | None = field(
        default=None,
        metadata={
            "name": "PointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
