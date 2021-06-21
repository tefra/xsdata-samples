from dataclasses import dataclass, field
from typing import List
from .direction_ref import DirectionRef
from .direction_type_enumeration import DirectionTypeEnumeration
from .flexible_line_ref import FlexibleLineRef
from .line_ref import LineRef
from .link_sequence_version_structure import LinkSequenceVersionStructure
from .points_on_route_rel_structure import PointsOnRouteRelStructure
from .route_ref_structure import RouteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RouteVersionStructure(LinkSequenceVersionStructure):
    class Meta:
        name = "Route_VersionStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DirectionType",
                    "type": DirectionTypeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DirectionRef",
                    "type": DirectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "pointsInSequence",
                    "type": PointsOnRouteRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InverseRouteRef",
                    "type": RouteRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 2,
        }
    )
