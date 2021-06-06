from dataclasses import dataclass, field
from typing import Optional
from .destination_display_ref import DestinationDisplayRef
from .destination_display_view import DestinationDisplayView
from .direction_ref import DirectionRef
from .direction_type_enumeration import DirectionTypeEnumeration
from .direction_view import DirectionView
from .journey_pattern_headways_rel_structure import JourneyPatternHeadwaysRelStructure
from .journey_pattern_layovers_rel_structure import JourneyPatternLayoversRelStructure
from .journey_pattern_refs_rel_structure import JourneyPatternRefsRelStructure
from .journey_pattern_run_times_rel_structure import JourneyPatternRunTimesRelStructure
from .journey_pattern_wait_times_rel_structure import JourneyPatternWaitTimesRelStructure
from .link_sequence_version_structure import LinkSequenceVersionStructure
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .operational_context_ref import OperationalContextRef
from .route_ref import RouteRef
from .route_view import RouteView
from .service_links_in_journey_pattern_rel_structure import ServiceLinksInJourneyPatternRelStructure
from .stop_points_in_journey_pattern_rel_structure import StopPointsInJourneyPatternRelStructure
from .timing_pattern_ref import TimingPatternRef
from .type_of_journey_pattern_ref import TypeOfJourneyPatternRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServicePatternVersionStructure(LinkSequenceVersionStructure):
    class Meta:
        name = "ServicePattern_VersionStructure"

    route_ref: Optional[RouteRef] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_view: Optional[RouteView] = field(
        default=None,
        metadata={
            "name": "RouteView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_type: Optional[DirectionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_ref: Optional[DirectionRef] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_view: Optional[DirectionView] = field(
        default=None,
        metadata={
            "name": "DirectionView",
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
    type_of_journey_pattern_ref: Optional[TypeOfJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "TypeOfJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operational_context_ref: Optional[OperationalContextRef] = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_pattern_ref: Optional[TimingPatternRef] = field(
        default=None,
        metadata={
            "name": "TimingPatternRef",
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
    run_times: Optional[JourneyPatternRunTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "runTimes",
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
    layovers: Optional[JourneyPatternLayoversRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_patterns: Optional[JourneyPatternRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "journeyPatterns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    points_in_sequence: Optional[StopPointsInJourneyPatternRelStructure] = field(
        default=None,
        metadata={
            "name": "pointsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    links_in_sequence: Optional[ServiceLinksInJourneyPatternRelStructure] = field(
        default=None,
        metadata={
            "name": "linksInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
