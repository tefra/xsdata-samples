from dataclasses import dataclass, field
from typing import Optional
from netex.models.infrastructure_link_version_structure import InfrastructureLinkVersionStructure
from netex.models.road_point_ref_structure import RoadPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoadElementVersionStructure(InfrastructureLinkVersionStructure):
    class Meta:
        name = "RoadElement_VersionStructure"

    from_point_ref: Optional[RoadPointRefStructure] = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_point_ref: Optional[RoadPointRefStructure] = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
