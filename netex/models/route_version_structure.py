from __future__ import annotations

from dataclasses import dataclass, field

from .direction_ref import DirectionRef
from .direction_type import DirectionType
from .flexible_line_ref import FlexibleLineRef
from .line_ref import LineRef
from .points_on_route_rel_structure import PointsOnRouteRelStructure
from .route_ref_structure import RouteRefStructure
from .sections_in_sequence_rel_structure import LinkSequenceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteVersionStructure(LinkSequenceVersionStructure):
    class Meta:
        name = "Route_VersionStructure"

    line_ref: None | FlexibleLineRef | LineRef = field(
        default=None,
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
            ),
        },
    )
    direction_type: None | DirectionType = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_ref: None | DirectionRef = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    points_in_sequence: None | PointsOnRouteRelStructure = field(
        default=None,
        metadata={
            "name": "pointsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    inverse_route_ref: None | RouteRefStructure = field(
        default=None,
        metadata={
            "name": "InverseRouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
