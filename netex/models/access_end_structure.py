from __future__ import annotations

from dataclasses import dataclass, field

from .all_modes_enumeration import AllModesEnumeration
from .place_ref_structure import PlaceRefStructure
from .point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessEndStructure:
    transport_mode: None | AllModesEnumeration = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    place_ref: None | PlaceRefStructure = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    point_ref: None | PointRefStructure = field(
        default=None,
        metadata={
            "name": "PointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
