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

    point_on_route_ref: Optional[PointOnRouteRef] = field(
        default=None,
        metadata={
            "name": "PointOnRouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    instruction: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Instruction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    path_heading: Optional[PathHeadingEnumeration] = field(
        default=None,
        metadata={
            "name": "PathHeading",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    heading: Optional[CompassBearing16Enumeration] = field(
        default=None,
        metadata={
            "name": "Heading",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bearing: Optional[float] = field(
        default=None,
        metadata={
            "name": "Bearing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transition: Optional[TransitionEnumeration] = field(
        default=None,
        metadata={
            "name": "Transition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    road_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "RoadName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    simple_feature_ref: Optional[SimpleFeatureRef] = field(
        default=None,
        metadata={
            "name": "SimpleFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
