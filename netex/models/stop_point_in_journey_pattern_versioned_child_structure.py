from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDuration

from .booking_arrangements_structure import BookingArrangementsStructure
from .destination_display_ref import DestinationDisplayRef
from .destination_display_view import DestinationDisplayView
from .dynamic_advertisement_enumeration import DynamicAdvertisementEnumeration
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .flexible_point_properties import FlexiblePointProperties
from .journey_pattern_headways_rel_structure import (
    JourneyPatternHeadwaysRelStructure,
)
from .journey_pattern_wait_times_rel_structure import (
    JourneyPatternWaitTimesRelStructure,
)
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .point_in_link_sequence_versioned_child_structure import (
    PointInLinkSequenceVersionedChildStructure,
)
from .request_method_type_enumeration import RequestMethodTypeEnumeration
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .service_link_ref_structure import ServiceLinkRefStructure
from .side_in_direction_of_travel_enumeration import (
    SideInDirectionOfTravelEnumeration,
)
from .stop_use_enumeration import StopUseEnumeration
from .timing_link_ref_structure import TimingLinkRefStructure
from .vias_rel_structure import ViasRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPointInJourneyPatternVersionedChildStructure(
    PointInLinkSequenceVersionedChildStructure
):
    class Meta:
        name = "StopPointInJourneyPattern_VersionedChildStructure"

    scheduled_stop_point_ref: FareScheduledStopPointRef | ScheduledStopPointRef | None = field(
        default=None,
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
                },
            ),
        },
    )
    onward_timing_link_ref: TimingLinkRefStructure | None = field(
        default=None,
        metadata={
            "name": "OnwardTimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_wait_point: bool | None = field(
        default=None,
        metadata={
            "name": "IsWaitPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wait_time_or_wait_times: XmlDuration | JourneyPatternWaitTimesRelStructure | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    headways: JourneyPatternHeadwaysRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    onward_service_link_ref: ServiceLinkRefStructure | None = field(
        default=None,
        metadata={
            "name": "OnwardServiceLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    for_alighting: bool | None = field(
        default=None,
        metadata={
            "name": "ForAlighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    for_boarding: bool | None = field(
        default=None,
        metadata={
            "name": "ForBoarding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alighting_side_in_direction_of_travel: SideInDirectionOfTravelEnumeration | None = field(
        default=None,
        metadata={
            "name": "AlightingSideInDirectionOfTravel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_side_in_direction_of_travel: SideInDirectionOfTravelEnumeration | None = field(
        default=None,
        metadata={
            "name": "BoardingSideInDirectionOfTravel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination_display_ref_or_destination_display_view: DestinationDisplayRef | DestinationDisplayView | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    vias: ViasRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_point_properties: FlexiblePointProperties | None = field(
        default=None,
        metadata={
            "name": "FlexiblePointProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    change_of_destination_display: bool | None = field(
        default=None,
        metadata={
            "name": "ChangeOfDestinationDisplay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    change_of_service_requirements: bool | None = field(
        default=None,
        metadata={
            "name": "ChangeOfServiceRequirements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: NoticeAssignmentsRelStructure | None = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    request_stop: bool | None = field(
        default=None,
        metadata={
            "name": "RequestStop",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    request_method: RequestMethodTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "RequestMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_use: StopUseEnumeration | None = field(
        default=None,
        metadata={
            "name": "StopUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_arrangements: BookingArrangementsStructure | None = field(
        default=None,
        metadata={
            "name": "BookingArrangements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    print: bool | None = field(
        default=None,
        metadata={
            "name": "Print",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    dynamic: DynamicAdvertisementEnumeration | None = field(
        default=None,
        metadata={
            "name": "Dynamic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
