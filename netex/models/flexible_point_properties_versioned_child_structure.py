from __future__ import annotations

from dataclasses import dataclass, field

from .activation_point_ref import ActivationPointRef
from .beacon_point_ref import BeaconPointRef
from .border_point_ref import BorderPointRef
from .entity_in_version_structure import VersionedChildStructure
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .garage_point_ref import GaragePointRef
from .parking_point_ref import ParkingPointRef
from .point_on_route_ref import PointOnRouteRef
from .point_ref import PointRef
from .railway_point_ref import RailwayPointRef
from .relief_point_ref import ReliefPointRef
from .road_point_ref import RoadPointRef
from .route_point_ref import RoutePointRef
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .timing_point_ref import TimingPointRef
from .traffic_control_point_ref import TrafficControlPointRef
from .vehicle_meeting_point_ref import VehicleMeetingPointRef
from .wire_point_ref import WirePointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexiblePointPropertiesVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "FlexiblePointProperties_VersionedChildStructure"

    choice: (
        None
        | PointOnRouteRef
        | VehicleMeetingPointRef
        | WirePointRef
        | RoadPointRef
        | RailwayPointRef
        | TrafficControlPointRef
        | BeaconPointRef
        | ActivationPointRef
        | BorderPointRef
        | FareScheduledStopPointRef
        | ScheduledStopPointRef
        | GaragePointRef
        | ParkingPointRef
        | ReliefPointRef
        | TimingPointRef
        | RoutePointRef
        | PointRef
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PointOnRouteRef",
                    "type": PointOnRouteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPointRef",
                    "type": VehicleMeetingPointRef,
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
                    "name": "PointRef",
                    "type": PointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    may_be_skipped: None | bool = field(
        default=None,
        metadata={
            "name": "MayBeSkipped",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    on_main_route: None | bool = field(
        default=None,
        metadata={
            "name": "OnMainRoute",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    point_standing_for_azone: None | bool = field(
        default=None,
        metadata={
            "name": "PointStandingForAZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    zone_containing_stops: None | bool = field(
        default=None,
        metadata={
            "name": "ZoneContainingStops",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
