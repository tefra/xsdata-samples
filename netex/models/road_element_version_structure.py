from dataclasses import dataclass, field

from .infrastructure_link_version_structure import (
    InfrastructureLinkVersionStructure,
)
from .road_point_ref_structure import RoadPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoadElementVersionStructure(InfrastructureLinkVersionStructure):
    class Meta:
        name = "RoadElement_VersionStructure"

    from_point_ref: RoadPointRefStructure | None = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    to_point_ref: RoadPointRefStructure | None = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
