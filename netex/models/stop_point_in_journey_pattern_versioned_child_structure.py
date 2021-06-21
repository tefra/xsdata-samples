from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlDuration
from .booking_arrangements_structure import BookingArrangementsStructure
from .destination_display_ref import DestinationDisplayRef
from .destination_display_view import DestinationDisplayView
from .dynamic_advertisement_enumeration import DynamicAdvertisementEnumeration
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .flexible_point_properties import FlexiblePointProperties
from .journey_pattern_headways_rel_structure import JourneyPatternHeadwaysRelStructure
from .journey_pattern_wait_times_rel_structure import JourneyPatternWaitTimesRelStructure
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .point_in_link_sequence_versioned_child_structure import PointInLinkSequenceVersionedChildStructure
from .request_method_type_enumeration import RequestMethodTypeEnumeration
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .service_link_ref_structure import ServiceLinkRefStructure
from .stop_use_enumeration import StopUseEnumeration
from .timing_link_ref_structure import TimingLinkRefStructure
from .vias_rel_structure import ViasRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPointInJourneyPatternVersionedChildStructure(PointInLinkSequenceVersionedChildStructure):
    class Meta:
        name = "StopPointInJourneyPattern_VersionedChildStructure"

    choice_1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                    "required": True,
                },
                {
                    "name": "OnwardTimingLinkRef",
                    "type": TimingLinkRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "IsWaitPoint",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaitTime",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "waitTimes",
                    "type": JourneyPatternWaitTimesRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "headways",
                    "type": JourneyPatternHeadwaysRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OnwardServiceLinkRef",
                    "type": ServiceLinkRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ForAlighting",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ForBoarding",
                    "type": bool,
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
            ),
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )
