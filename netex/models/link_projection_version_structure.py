from dataclasses import dataclass, field
from typing import Optional
from netex.models.link_ref_structure import LinkRefStructure
from netex.models.point_on_link_by_value_structure import PointOnLinkByValueStructure
from netex.models.point_on_link_ref_structure_2 import PointOnLinkRefStructure2
from netex.models.projection_version_structure import ProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkProjectionVersionStructure(ProjectionVersionStructure):
    class Meta:
        name = "LinkProjection_VersionStructure"

    projected_link_ref: Optional[LinkRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectedLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    project_to_link_ref: Optional[LinkRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectToLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_point_on_link_ref: Optional[PointOnLinkRefStructure2] = field(
        default=None,
        metadata={
            "name": "StartPointOnLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_point_on_link_by_value: Optional[PointOnLinkByValueStructure] = field(
        default=None,
        metadata={
            "name": "StartPointOnLinkByValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_point_on_link_ref: Optional[PointOnLinkRefStructure2] = field(
        default=None,
        metadata={
            "name": "EndPointOnLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_point_on_link_by_value: Optional[PointOnLinkByValueStructure] = field(
        default=None,
        metadata={
            "name": "EndPointOnLinkByValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
