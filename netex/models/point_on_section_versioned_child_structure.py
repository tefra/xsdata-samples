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

    border_point_ref: Optional[BorderPointRef] = field(
        default=None,
        metadata={
            "name": "BorderPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_scheduled_stop_point_ref: Optional[FareScheduledStopPointRef] = field(
        default=None,
        metadata={
            "name": "FareScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    scheduled_stop_point_ref: Optional[ScheduledStopPointRef] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    garage_point_ref: Optional[GaragePointRef] = field(
        default=None,
        metadata={
            "name": "GaragePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_point_ref: Optional[ParkingPointRef] = field(
        default=None,
        metadata={
            "name": "ParkingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    relief_point_ref: Optional[ReliefPointRef] = field(
        default=None,
        metadata={
            "name": "ReliefPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_point_ref: Optional[TimingPointRef] = field(
        default=None,
        metadata={
            "name": "TimingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_point_ref: Optional[RoutePointRef] = field(
        default=None,
        metadata={
            "name": "RoutePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wire_point_ref: Optional[WirePointRef] = field(
        default=None,
        metadata={
            "name": "WirePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_point_ref: Optional[RoadPointRef] = field(
        default=None,
        metadata={
            "name": "RoadPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    railway_point_ref: Optional[RailwayPointRef] = field(
        default=None,
        metadata={
            "name": "RailwayPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    traffic_control_point_ref: Optional[TrafficControlPointRef] = field(
        default=None,
        metadata={
            "name": "TrafficControlPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    beacon_point_ref: Optional[BeaconPointRef] = field(
        default=None,
        metadata={
            "name": "BeaconPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_point_ref: Optional[ActivationPointRef] = field(
        default=None,
        metadata={
            "name": "ActivationPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_ref: Optional[PointRef] = field(
        default=None,
        metadata={
            "name": "PointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    border_point: Optional[BorderPoint] = field(
        default=None,
        metadata={
            "name": "BorderPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_scheduled_stop_point: Optional[FareScheduledStopPoint] = field(
        default=None,
        metadata={
            "name": "FareScheduledStopPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    scheduled_stop_point: Optional[ScheduledStopPoint] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_junction: Optional[PathJunction] = field(
        default=None,
        metadata={
            "name": "PathJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_point: Optional[RoutePoint] = field(
        default=None,
        metadata={
            "name": "RoutePoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_point: Optional[ParkingPoint] = field(
        default=None,
        metadata={
            "name": "ParkingPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    garage_point: Optional[GaragePoint] = field(
        default=None,
        metadata={
            "name": "GaragePoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    relief_point: Optional[ReliefPoint] = field(
        default=None,
        metadata={
            "name": "ReliefPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_point: Optional[TimingPoint] = field(
        default=None,
        metadata={
            "name": "TimingPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wire_junction: Optional[WireJunction] = field(
        default=None,
        metadata={
            "name": "WireJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_junction: Optional[RoadJunction] = field(
        default=None,
        metadata={
            "name": "RoadJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    railway_junction: Optional[RailwayJunction] = field(
        default=None,
        metadata={
            "name": "RailwayJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    traffic_control_point: Optional[TrafficControlPoint] = field(
        default=None,
        metadata={
            "name": "TrafficControlPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    beacon_point: Optional[BeaconPoint] = field(
        default=None,
        metadata={
            "name": "BeaconPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_point: Optional[ActivationPoint] = field(
        default=None,
        metadata={
            "name": "ActivationPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point: Optional[Point2] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
