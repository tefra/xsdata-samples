from dataclasses import dataclass, field
from decimal import Decimal

from .line_string import LineString
from .link_sequence_ref_structure import LinkSequenceRefStructure
from .point_refs_rel_structure import PointRefsRelStructure
from .projection_version_structure import ProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkSequenceProjectionVersionStructure(ProjectionVersionStructure):
    class Meta:
        name = "LinkSequenceProjection_VersionStructure"

    projected_link_sequence_ref: LinkSequenceRefStructure | None = field(
        default=None,
        metadata={
            "name": "ProjectedLinkSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance: Decimal | None = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    points_or_line_string: PointRefsRelStructure | LineString | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "points",
                    "type": PointRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineString",
                    "type": LineString,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
            ),
        },
    )
