from __future__ import annotations

from dataclasses import dataclass, field

from .point_version_structure import PointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoutePointVersionStructure(PointVersionStructure):
    class Meta:
        name = "RoutePoint_VersionStructure"

    via_flag: None | bool = field(
        default=None,
        metadata={
            "name": "ViaFlag",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    border_crossing: None | bool = field(
        default=None,
        metadata={
            "name": "BorderCrossing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
