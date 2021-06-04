from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.models.line_string import LineString
from netex.models.link_sequence_ref_structure import LinkSequenceRefStructure
from netex.models.point_refs_rel_structure import PointRefsRelStructure
from netex.models.projection_version_structure import ProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkSequenceProjectionVersionStructure(ProjectionVersionStructure):
    class Meta:
        name = "LinkSequenceProjection_VersionStructure"

    projected_link_sequence_ref: Optional[LinkSequenceRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectedLinkSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    points: Optional[PointRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
