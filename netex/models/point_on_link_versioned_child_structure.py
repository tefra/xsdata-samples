from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from netex.models.activation_point_1 import ActivationPoint1
from netex.models.activation_point_2 import ActivationPoint2
from netex.models.activation_point_ref import ActivationPointRef
from netex.models.alternative_texts_rel_structure import VersionedChildStructure
from netex.models.beacon_point import BeaconPoint
from netex.models.beacon_point_ref import BeaconPointRef
from netex.models.border_point import BorderPoint
from netex.models.border_point_ref import BorderPointRef
from netex.models.fare_scheduled_stop_point import FareScheduledStopPoint
from netex.models.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.models.garage_point import GaragePoint
from netex.models.garage_point_ref import GaragePointRef
from netex.models.infrastructure_point import InfrastructurePoint
from netex.models.infrastructure_point_ref import InfrastructurePointRef
from netex.models.link_ref_structure import LinkRefStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.parking_point_1 import ParkingPoint1
from netex.models.parking_point_2 import ParkingPoint2
from netex.models.parking_point_ref import ParkingPointRef
from netex.models.path_junction import PathJunction
from netex.models.point_2 import Point2
from netex.models.point_on_link_ref import PointOnLinkRef
from netex.models.point_ref import PointRef
from netex.models.railway_junction import RailwayJunction
from netex.models.railway_point_ref import RailwayPointRef
from netex.models.relief_point_1 import ReliefPoint1
from netex.models.relief_point_2 import ReliefPoint2
from netex.models.relief_point_ref import ReliefPointRef
from netex.models.road_junction import RoadJunction
from netex.models.road_point_ref import RoadPointRef
from netex.models.route_point import RoutePoint
from netex.models.route_point_ref import RoutePointRef
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.timing_point_1 import TimingPoint1
from netex.models.timing_point_2 import TimingPoint2
from netex.models.timing_point_ref import TimingPointRef
from netex.models.traffic_control_point import TrafficControlPoint
from netex.models.traffic_control_point_ref import TrafficControlPointRef
from netex.models.wire_junction import WireJunction
from netex.models.wire_point_ref import WirePointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOnLinkVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "PointOnLink_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    link_ref: Optional[LinkRefStructure] = field(
        default=None,
        metadata={
            "name": "LinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_from_start: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DistanceFromStart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    border_point_ref: List[BorderPointRef] = field(
        default_factory=list,
        metadata={
            "name": "BorderPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    fare_scheduled_stop_point_ref: List[FareScheduledStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "FareScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 5,
            "sequential": True,
        }
    )
    scheduled_stop_point_ref: List[ScheduledStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    garage_point_ref: List[GaragePointRef] = field(
        default_factory=list,
        metadata={
            "name": "GaragePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    parking_point_ref: List[ParkingPointRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 5,
            "sequential": True,
        }
    )
    relief_point_ref: List[ReliefPointRef] = field(
        default_factory=list,
        metadata={
            "name": "ReliefPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    timing_point_ref: List[TimingPointRef] = field(
        default_factory=list,
        metadata={
            "name": "TimingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    route_point_ref: List[RoutePointRef] = field(
        default_factory=list,
        metadata={
            "name": "RoutePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    wire_point_ref: List[WirePointRef] = field(
        default_factory=list,
        metadata={
            "name": "WirePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    road_point_ref: List[RoadPointRef] = field(
        default_factory=list,
        metadata={
            "name": "RoadPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    railway_point_ref: List[RailwayPointRef] = field(
        default_factory=list,
        metadata={
            "name": "RailwayPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    infrastructure_point_ref: List[InfrastructurePointRef] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructurePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    traffic_control_point_ref: List[TrafficControlPointRef] = field(
        default_factory=list,
        metadata={
            "name": "TrafficControlPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    beacon_point_ref: List[BeaconPointRef] = field(
        default_factory=list,
        metadata={
            "name": "BeaconPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    activation_point_ref: List[ActivationPointRef] = field(
        default_factory=list,
        metadata={
            "name": "ActivationPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    point_on_link_ref: List[PointOnLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOnLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
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
    border_point: List[BorderPoint] = field(
        default_factory=list,
        metadata={
            "name": "BorderPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    fare_scheduled_stop_point: List[FareScheduledStopPoint] = field(
        default_factory=list,
        metadata={
            "name": "FareScheduledStopPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    scheduled_stop_point: List[ScheduledStopPoint] = field(
        default_factory=list,
        metadata={
            "name": "ScheduledStopPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    path_junction: List[PathJunction] = field(
        default_factory=list,
        metadata={
            "name": "PathJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    route_point: List[RoutePoint] = field(
        default_factory=list,
        metadata={
            "name": "RoutePoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    parking_point: List[ParkingPoint2] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    garage_point: List[GaragePoint] = field(
        default_factory=list,
        metadata={
            "name": "GaragePoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 5,
            "sequential": True,
        }
    )
    netex_org_uk_netex_parking_point: List[ParkingPoint1] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPoint_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    relief_point: List[ReliefPoint2] = field(
        default_factory=list,
        metadata={
            "name": "ReliefPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    netex_org_uk_netex_relief_point: List[ReliefPoint1] = field(
        default_factory=list,
        metadata={
            "name": "ReliefPoint_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    timing_point: List[TimingPoint2] = field(
        default_factory=list,
        metadata={
            "name": "TimingPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    netex_org_uk_netex_timing_point: List[TimingPoint1] = field(
        default_factory=list,
        metadata={
            "name": "TimingPoint_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    wire_junction: List[WireJunction] = field(
        default_factory=list,
        metadata={
            "name": "WireJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    road_junction: List[RoadJunction] = field(
        default_factory=list,
        metadata={
            "name": "RoadJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    railway_junction: List[RailwayJunction] = field(
        default_factory=list,
        metadata={
            "name": "RailwayJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    infrastructure_point: List[InfrastructurePoint] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructurePoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    traffic_control_point: List[TrafficControlPoint] = field(
        default_factory=list,
        metadata={
            "name": "TrafficControlPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    beacon_point: List[BeaconPoint] = field(
        default_factory=list,
        metadata={
            "name": "BeaconPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    activation_point: List[ActivationPoint2] = field(
        default_factory=list,
        metadata={
            "name": "ActivationPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    netex_org_uk_netex_activation_point: List[ActivationPoint1] = field(
        default_factory=list,
        metadata={
            "name": "ActivationPoint_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
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
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
