from __future__ import annotations

from dataclasses import dataclass, field

from .destination_display_ref import DestinationDisplayRef
from .destination_display_view import DestinationDisplayView
from .direction_ref import DirectionRef
from .direction_type_enumeration import DirectionTypeEnumeration
from .direction_view import DirectionView
from .journey_pattern_headways_rel_structure import (
    JourneyPatternHeadwaysRelStructure,
)
from .journey_pattern_layovers_rel_structure import (
    JourneyPatternLayoversRelStructure,
)
from .journey_pattern_refs_rel_structure import JourneyPatternRefsRelStructure
from .journey_pattern_run_times_rel_structure import (
    JourneyPatternRunTimesRelStructure,
)
from .journey_pattern_wait_times_rel_structure import (
    JourneyPatternWaitTimesRelStructure,
)
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .operational_context_ref import OperationalContextRef
from .route_ref import RouteRef
from .route_view import RouteView
from .sections_in_sequence_rel_structure import LinkSequenceVersionStructure
from .service_links_in_journey_pattern_rel_structure import (
    ServiceLinksInJourneyPatternRelStructure,
)
from .stop_points_in_journey_pattern_rel_structure import (
    StopPointsInJourneyPatternRelStructure,
)
from .timing_pattern_ref import TimingPatternRef
from .type_of_journey_pattern_ref import TypeOfJourneyPatternRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServicePatternVersionStructure(LinkSequenceVersionStructure):
    class Meta:
        name = "ServicePattern_VersionStructure"

    route_ref_or_route_view: RouteRef | RouteView | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RouteRef",
                    "type": RouteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RouteView",
                    "type": RouteView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    direction_type: DirectionTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_ref_or_direction_view: DirectionRef | DirectionView | None = (
        field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "DirectionRef",
                        "type": DirectionRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "DirectionView",
                        "type": DirectionView,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
    )
    destination_display_ref_or_destination_display_view: (
        DestinationDisplayRef | DestinationDisplayView | None
    ) = field(
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
    type_of_journey_pattern_ref: TypeOfJourneyPatternRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operational_context_ref: OperationalContextRef | None = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timing_pattern_ref: TimingPatternRef | None = field(
        default=None,
        metadata={
            "name": "TimingPatternRef",
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
    run_times: JourneyPatternRunTimesRelStructure | None = field(
        default=None,
        metadata={
            "name": "runTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wait_times: JourneyPatternWaitTimesRelStructure | None = field(
        default=None,
        metadata={
            "name": "waitTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    headways: JourneyPatternHeadwaysRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    layovers: JourneyPatternLayoversRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_patterns: JourneyPatternRefsRelStructure | None = field(
        default=None,
        metadata={
            "name": "journeyPatterns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    points_in_sequence: StopPointsInJourneyPatternRelStructure | None = field(
        default=None,
        metadata={
            "name": "pointsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    links_in_sequence: ServiceLinksInJourneyPatternRelStructure | None = field(
        default=None,
        metadata={
            "name": "linksInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
