from __future__ import annotations

from dataclasses import dataclass, field

from .infrastructure_link_version_structure import (
    InfrastructureLinkVersionStructure,
)
from .railway_point_ref_structure import RailwayPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RailwayElementVersionStructure(InfrastructureLinkVersionStructure):
    class Meta:
        name = "RailwayElement_VersionStructure"

    from_point_ref: RailwayPointRefStructure = field(
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_point_ref: RailwayPointRefStructure = field(
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
