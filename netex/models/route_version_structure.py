from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.direction_ref import DirectionRef
from netex.models.direction_type_enumeration import DirectionTypeEnumeration
from netex.models.flexible_line_ref import FlexibleLineRef
from netex.models.line_ref import LineRef
from netex.models.link_sequence_version_structure import LinkSequenceVersionStructure
from netex.models.points_on_route_rel_structure import PointsOnRouteRelStructure
from netex.models.route_ref_structure import RouteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RouteVersionStructure(LinkSequenceVersionStructure):
    class Meta:
        name = "Route_VersionStructure"

    flexible_line_ref: List[FlexibleLineRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
        }
    )
    line_ref: Optional[LineRef] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_type: Optional[DirectionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_ref: Optional[DirectionRef] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    points_in_sequence: Optional[PointsOnRouteRelStructure] = field(
        default=None,
        metadata={
            "name": "pointsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    inverse_route_ref: Optional[RouteRefStructure] = field(
        default=None,
        metadata={
            "name": "InverseRouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
