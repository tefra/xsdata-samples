from dataclasses import dataclass, field
from typing import List, Optional
from .activation_point_ref import ActivationPointRef
from .alternative_texts_rel_structure import VersionedChildStructure
from .beacon_point_ref import BeaconPointRef
from .booking_arrangements_structure import BookingArrangementsStructure
from .border_point_ref import BorderPointRef
from .dead_run_call_part_structure import DeadRunCallPartStructure
from .destination_display_ref import DestinationDisplayRef
from .destination_display_view import DestinationDisplayView
from .dynamic_advertisement_enumeration import DynamicAdvertisementEnumeration
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .flexible_point_properties import FlexiblePointProperties
from .garage_point_ref import GaragePointRef
from .infrastructure_point_ref import InfrastructurePointRef
from .multilingual_string import MultilingualString
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .parking_point_ref import ParkingPointRef
from .point_in_journey_pattern_ref_structure import PointInJourneyPatternRefStructure
from .point_on_link_ref import PointOnLinkRef
from .point_ref import PointRef
from .railway_point_ref import RailwayPointRef
from .relief_point_ref import ReliefPointRef
from .request_method_type_enumeration import RequestMethodTypeEnumeration
from .road_point_ref import RoadPointRef
from .route_point_ref import RoutePointRef
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .scheduled_stop_point_view import ScheduledStopPointView
from .stop_use_enumeration import StopUseEnumeration
from .timing_point_ref import TimingPointRef
from .traffic_control_point_ref import TrafficControlPointRef
from .vias_rel_structure import ViasRelStructure
from .wire_point_ref import WirePointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeadRunCallVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "DeadRunCall_VersionedChildStructure"

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
                {
                    "name": "ScheduledStopPointView",
                    "type": ScheduledStopPointView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointInJourneyPatternRef",
                    "type": PointInJourneyPatternRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Arrival",
                    "type": DeadRunCallPartStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Departure",
                    "type": DeadRunCallPartStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplayRef",
                    "type": DestinationDisplayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplayView",
                    "type": DestinationDisplayView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "vias",
                    "type": ViasRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexiblePointProperties",
                    "type": FlexiblePointProperties,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChangeOfDestinationDisplay",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChangeOfServiceRequirements",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "noticeAssignments",
                    "type": NoticeAssignmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RequestStop",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RequestMethod",
                    "type": RequestMethodTypeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopUse",
                    "type": StopUseEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BookingArrangements",
                    "type": BookingArrangementsStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Print",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Dynamic",
                    "type": DynamicAdvertisementEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Note",
                    "type": MultilingualString,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 72,
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
