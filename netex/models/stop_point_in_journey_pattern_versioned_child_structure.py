from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from netex.models.booking_arrangements_structure import BookingArrangementsStructure
from netex.models.destination_display_ref import DestinationDisplayRef
from netex.models.destination_display_view import DestinationDisplayView
from netex.models.dynamic_advertisement_enumeration import DynamicAdvertisementEnumeration
from netex.models.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.models.flexible_point_properties import FlexiblePointProperties
from netex.models.journey_pattern_headways_rel_structure import JourneyPatternHeadwaysRelStructure
from netex.models.journey_pattern_wait_times_rel_structure import JourneyPatternWaitTimesRelStructure
from netex.models.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.models.point_in_link_sequence_versioned_child_structure import PointInLinkSequenceVersionedChildStructure
from netex.models.request_method_type_enumeration import RequestMethodTypeEnumeration
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.service_link_ref_structure import ServiceLinkRefStructure
from netex.models.stop_use_enumeration import StopUseEnumeration
from netex.models.timing_link_ref_structure import TimingLinkRefStructure
from netex.models.vias_rel_structure import ViasRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPointInJourneyPatternVersionedChildStructure(PointInLinkSequenceVersionedChildStructure):
    class Meta:
        name = "StopPointInJourneyPattern_VersionedChildStructure"

    fare_scheduled_stop_point_ref: List[FareScheduledStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "FareScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )
    scheduled_stop_point_ref: Optional[ScheduledStopPointRef] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    onward_timing_link_ref: Optional[TimingLinkRefStructure] = field(
        default=None,
        metadata={
            "name": "OnwardTimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_wait_point: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsWaitPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "WaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wait_times: Optional[JourneyPatternWaitTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "waitTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    headways: Optional[JourneyPatternHeadwaysRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    onward_service_link_ref: Optional[ServiceLinkRefStructure] = field(
        default=None,
        metadata={
            "name": "OnwardServiceLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    for_alighting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForAlighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    for_boarding: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForBoarding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_ref: Optional[DestinationDisplayRef] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_view: Optional[DestinationDisplayView] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vias: Optional[ViasRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_point_properties: Optional[FlexiblePointProperties] = field(
        default=None,
        metadata={
            "name": "FlexiblePointProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    change_of_destination_display: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChangeOfDestinationDisplay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    change_of_service_requirements: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChangeOfServiceRequirements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    request_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequestStop",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    request_method: Optional[RequestMethodTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RequestMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_use: Optional[StopUseEnumeration] = field(
        default=None,
        metadata={
            "name": "StopUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_arrangements: Optional[BookingArrangementsStructure] = field(
        default=None,
        metadata={
            "name": "BookingArrangements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    print: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Print",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dynamic: Optional[DynamicAdvertisementEnumeration] = field(
        default=None,
        metadata={
            "name": "Dynamic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
