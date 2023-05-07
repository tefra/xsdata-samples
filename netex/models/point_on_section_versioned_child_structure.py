from dataclasses import dataclass, field
from typing import Optional
from .activation_link_ref import ActivationLinkRef
from .activation_point import ActivationPoint
from .activation_point_ref import ActivationPointRef
from .beacon_point import BeaconPoint
from .beacon_point_ref import BeaconPointRef
from .border_point import BorderPoint
from .border_point_ref import BorderPointRef
from .fare_scheduled_stop_point import FareScheduledStopPoint
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .garage_point import GaragePoint
from .garage_point_ref import GaragePointRef
from .line_link_ref import LineLinkRef
from .parking_point import ParkingPoint
from .parking_point_ref import ParkingPointRef
from .path_junction import PathJunction
from .path_link_ref import PathLinkRef
from .point_2 import Point2
from .point_in_link_sequence_versioned_child_structure import PointInLinkSequenceVersionedChildStructure
from .point_ref import PointRef
from .railway_junction import RailwayJunction
from .railway_link_ref import RailwayLinkRef
from .railway_point_ref import RailwayPointRef
from .relief_point import ReliefPoint
from .relief_point_ref import ReliefPointRef
from .road_junction import RoadJunction
from .road_link_ref import RoadLinkRef
from .road_point_ref import RoadPointRef
from .route_link_ref import RouteLinkRef
from .route_point import RoutePoint
from .route_point_ref import RoutePointRef
from .scheduled_stop_point import ScheduledStopPoint
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .service_link_ref import ServiceLinkRef
from .timing_link_ref import TimingLinkRef
from .timing_point import TimingPoint
from .timing_point_ref import TimingPointRef
from .traffic_control_point import TrafficControlPoint
from .traffic_control_point_ref import TrafficControlPointRef
from .wire_junction import WireJunction
from .wire_link_ref import WireLinkRef
from .wire_point_ref import WirePointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOnSectionVersionedChildStructure(PointInLinkSequenceVersionedChildStructure):
    class Meta:
        name = "PointOnSection_VersionedChildStructure"

    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BorderPointRef",
                    "type": BorderPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GaragePointRef",
                    "type": GaragePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPointRef",
                    "type": ParkingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPointRef",
                    "type": ReliefPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointRef",
                    "type": TimingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutePointRef",
                    "type": RoutePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WirePointRef",
                    "type": WirePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadPointRef",
                    "type": RoadPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayPointRef",
                    "type": RailwayPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrafficControlPointRef",
                    "type": TrafficControlPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BeaconPointRef",
                    "type": BeaconPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationPointRef",
                    "type": ActivationPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointRef",
                    "type": PointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BorderPoint",
                    "type": BorderPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareScheduledStopPoint",
                    "type": FareScheduledStopPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPoint",
                    "type": ScheduledStopPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathJunction",
                    "type": PathJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutePoint",
                    "type": RoutePoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPoint",
                    "type": ParkingPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GaragePoint",
                    "type": GaragePoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPoint",
                    "type": ReliefPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPoint",
                    "type": TimingPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireJunction",
                    "type": WireJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadJunction",
                    "type": RoadJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailwayJunction",
                    "type": RailwayJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrafficControlPoint",
                    "type": TrafficControlPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BeaconPoint",
                    "type": BeaconPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationPoint",
                    "type": ActivationPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Point",
                    "type": Point2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    service_link_ref: Optional[ServiceLinkRef] = field(
        default=None,
        metadata={
            "name": "ServiceLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_link_ref: Optional[LineLinkRef] = field(
        default=None,
        metadata={
            "name": "LineLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_link_ref: Optional[PathLinkRef] = field(
        default=None,
        metadata={
            "name": "PathLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_link_ref: Optional[TimingLinkRef] = field(
        default=None,
        metadata={
            "name": "TimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_link_ref: Optional[RouteLinkRef] = field(
        default=None,
        metadata={
            "name": "RouteLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wire_link_ref: Optional[WireLinkRef] = field(
        default=None,
        metadata={
            "name": "WireLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_link_ref: Optional[RoadLinkRef] = field(
        default=None,
        metadata={
            "name": "RoadLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    railway_link_ref: Optional[RailwayLinkRef] = field(
        default=None,
        metadata={
            "name": "RailwayLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_link_ref: Optional[ActivationLinkRef] = field(
        default=None,
        metadata={
            "name": "ActivationLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    reverse: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reverse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
