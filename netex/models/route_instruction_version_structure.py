from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .compass_bearing16_enumeration import CompassBearing16Enumeration
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .path_heading_enumeration import PathHeadingEnumeration
from .point_on_route_ref import PointOnRouteRef
from .simple_feature_ref import SimpleFeatureRef
from .transition_enumeration import TransitionEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RouteInstructionVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "RouteInstruction_VersionStructure"

    point_on_route_ref: PointOnRouteRef | None = field(
        default=None,
        metadata={
            "name": "PointOnRouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    instruction: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Instruction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    path_heading: PathHeadingEnumeration | None = field(
        default=None,
        metadata={
            "name": "PathHeading",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    heading: CompassBearing16Enumeration | None = field(
        default=None,
        metadata={
            "name": "Heading",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bearing: float | None = field(
        default=None,
        metadata={
            "name": "Bearing",
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
    transition: TransitionEnumeration | None = field(
        default=None,
        metadata={
            "name": "Transition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    road_name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "RoadName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    simple_feature_ref: SimpleFeatureRef | None = field(
        default=None,
        metadata={
            "name": "SimpleFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
