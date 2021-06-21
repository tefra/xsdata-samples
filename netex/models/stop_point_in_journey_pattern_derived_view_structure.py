from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from .derived_view_structure import DerivedViewStructure
from .fare_point_in_pattern_ref import FarePointInPatternRef
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .onward_service_link_view import OnwardServiceLinkView
from .onward_timing_link_view import OnwardTimingLinkView
from .point_in_journey_pattern_ref import PointInJourneyPatternRef
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

    fare_point_in_pattern_ref: Optional[FarePointInPatternRef] = field(
        default=None,
        metadata={
            "name": "FarePointInPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_point_in_journey_pattern_ref: Optional[StopPointInJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "StopPointInJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_point_in_journey_pattern_ref: Optional[TimingPointInJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "TimingPointInJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_in_journey_pattern_ref: Optional[PointInJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "PointInJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    visit_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "VisitNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: List[object] = field(
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
                },
                {
                    "name": "ScheduledStopPointView",
                    "type": ScheduledStopPointView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OnwardTimingLinkView",
                    "type": OnwardTimingLinkView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "TimingPointStatus",
                    "type": TimingPointStatusEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "IsWaitPoint",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "WaitTime",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledHeadwayInterval",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MinimumHeadwayInterval",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MaximumHeadwayInterval",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 2,
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
