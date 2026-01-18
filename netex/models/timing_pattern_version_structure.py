from dataclasses import dataclass, field

from .direction_type import DirectionType
from .route_ref_structure import RouteRefStructure
from .sections_in_sequence_rel_structure import LinkSequenceVersionStructure
from .time_demand_type_ref import TimeDemandTypeRef
from .timeband_ref import TimebandRef
from .timing_links_rel_structure import TimingLinksRelStructure
from .timing_points_in_journey_pattern_rel_structure import (
    TimingPointsInJourneyPatternRelStructure,
)
from .timing_points_rel_structure import TimingPointsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingPatternVersionStructure(LinkSequenceVersionStructure):
    class Meta:
        name = "TimingPattern_VersionStructure"

    route_ref: RouteRefStructure | None = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_type: DirectionType | None = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_demand_type_ref_or_timeband_ref: (
        TimeDemandTypeRef | TimebandRef | None
    ) = field(
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
    points_in_sequence: TimingPointsInJourneyPatternRelStructure | None = (
        field(
            default=None,
            metadata={
                "name": "pointsInSequence",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    points: TimingPointsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    links: TimingLinksRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
