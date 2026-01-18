from __future__ import annotations

from dataclasses import dataclass, field

from .infrastructure_link_version_structure import (
    InfrastructureLinkVersionStructure,
)
from .railway_point_ref_structure import RailwayPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RailwayElementVersionStructure(InfrastructureLinkVersionStructure):
    class Meta:
        name = "RailwayElement_VersionStructure"

    from_point_ref: None | RailwayPointRefStructure = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    to_point_ref: None | RailwayPointRefStructure = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
