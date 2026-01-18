from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

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

    point_on_route_ref: None | PointOnRouteRef = field(
        default=None,
        metadata={
            "name": "PointOnRouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    instruction: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Instruction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    path_heading: None | PathHeadingEnumeration = field(
        default=None,
        metadata={
            "name": "PathHeading",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    heading: None | CompassBearing16Enumeration = field(
        default=None,
        metadata={
            "name": "Heading",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bearing: None | float = field(
        default=None,
        metadata={
            "name": "Bearing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance: None | Decimal = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transition: None | TransitionEnumeration = field(
        default=None,
        metadata={
            "name": "Transition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    road_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "RoadName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    simple_feature_ref: None | SimpleFeatureRef = field(
        default=None,
        metadata={
            "name": "SimpleFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
