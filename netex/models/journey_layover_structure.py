from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from .activation_point_ref import ActivationPointRef
from .beacon_point_ref import BeaconPointRef
from .border_point_ref import BorderPointRef
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .garage_point_ref import GaragePointRef
from .infrastructure_point_ref import InfrastructurePointRef
from .journey_timing_versioned_child_structure import JourneyTimingVersionedChildStructure
from .parking_point_ref import ParkingPointRef
from .point_on_link_ref import PointOnLinkRef
from .point_ref import PointRef
from .railway_point_ref import RailwayPointRef
from .relief_point_ref import ReliefPointRef
from .road_point_ref import RoadPointRef
from .route_point_ref import RoutePointRef
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .timing_point_ref import TimingPointRef
from .traffic_control_point_ref import TrafficControlPointRef
from .wire_point_ref import WirePointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyLayoverStructure(JourneyTimingVersionedChildStructure):
    layover: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Layover",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    choice: List[object] = field(
        default_factory=list,
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
                    "name": "InfrastructurePointRef",
                    "type": InfrastructurePointRef,
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
                    "name": "PointOnLinkRef",
                    "type": PointOnLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointRef",
                    "type": PointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "min_occurs": 17,
            "max_occurs": 54,
        }
    )
