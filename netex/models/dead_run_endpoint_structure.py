from dataclasses import dataclass, field
from typing import Optional
from netex.models.activation_point_ref import ActivationPointRef
from netex.models.beacon_point_ref import BeaconPointRef
from netex.models.border_point_ref import BorderPointRef
from netex.models.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.models.garage_point_ref import GaragePointRef
from netex.models.infrastructure_point_ref import InfrastructurePointRef
from netex.models.parking_point_ref import ParkingPointRef
from netex.models.point_on_link_ref import PointOnLinkRef
from netex.models.point_ref import PointRef
from netex.models.railway_point_ref import RailwayPointRef
from netex.models.relief_point_ref import ReliefPointRef
from netex.models.road_point_ref import RoadPointRef
from netex.models.route_point_ref import RoutePointRef
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.timing_point_ref import TimingPointRef
from netex.models.traffic_control_point_ref import TrafficControlPointRef
from netex.models.type_of_point_ref import TypeOfPointRef
from netex.models.wire_point_ref import WirePointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeadRunEndpointStructure:
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
    infrastructure_point_ref: Optional[InfrastructurePointRef] = field(
        default=None,
        metadata={
            "name": "InfrastructurePointRef",
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
    point_on_link_ref: Optional[PointOnLinkRef] = field(
        default=None,
        metadata={
            "name": "PointOnLinkRef",
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
    type_of_point_ref: Optional[TypeOfPointRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
