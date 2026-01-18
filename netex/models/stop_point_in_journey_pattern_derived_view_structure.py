from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDuration

from .derived_view_structure import DerivedViewStructure
from .fare_point_in_pattern_ref import FarePointInPatternRef
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .onward_service_link_view import OnwardServiceLinkView
from .onward_timing_link_view import OnwardTimingLinkView
from .point_in_journey_pattern_ref import PointInJourneyPatternRef
from .point_in_single_journey_path_ref import PointInSingleJourneyPathRef
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .scheduled_stop_point_view import ScheduledStopPointView
from .service_link_ref_structure import ServiceLinkRefStructure
from .stop_point_in_journey_pattern_ref import StopPointInJourneyPatternRef
from .time_demand_type_ref import TimeDemandTypeRef
from .timeband_ref import TimebandRef
from .timing_point_in_journey_pattern_ref import TimingPointInJourneyPatternRef
from .timing_point_status_enumeration import TimingPointStatusEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPointInJourneyPatternDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "StopPointInJourneyPattern_DerivedViewStructure"

    point_in_journey_pattern_ref: PointInSingleJourneyPathRef | FarePointInPatternRef | StopPointInJourneyPatternRef | TimingPointInJourneyPatternRef | PointInJourneyPatternRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PointInSingleJourneyPathRef",
                    "type": PointInSingleJourneyPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FarePointInPatternRef",
                    "type": FarePointInPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPointInJourneyPatternRef",
                    "type": StopPointInJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointInJourneyPatternRef",
                    "type": TimingPointInJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointInJourneyPatternRef",
                    "type": PointInJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    visit_number: int | None = field(
        default=None,
        metadata={
            "name": "VisitNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view: FareScheduledStopPointRef | ScheduledStopPointRef | ScheduledStopPointView | None = field(
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
                {
                    "name": "ScheduledStopPointView",
                    "type": ScheduledStopPointView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    onward_timing_link_view: OnwardTimingLinkView | None = field(
        default=None,
        metadata={
            "name": "OnwardTimingLinkView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    onward_service_link_ref_or_onward_service_link_view: ServiceLinkRefStructure | OnwardServiceLinkView | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OnwardServiceLinkRef",
                    "type": ServiceLinkRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OnwardServiceLinkView",
                    "type": OnwardServiceLinkView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    timing_point_status: TimingPointStatusEnumeration | None = field(
        default=None,
        metadata={
            "name": "TimingPointStatus",
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
    time_demand_type_ref_or_timeband_ref: TimeDemandTypeRef | TimebandRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TimeDemandTypeRef",
                    "type": TimeDemandTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimebandRef",
                    "type": TimebandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    wait_time: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "WaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    scheduled_headway_interval: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "ScheduledHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_headway_interval: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "MinimumHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_headway_interval: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "MaximumHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
