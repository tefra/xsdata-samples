from dataclasses import dataclass, field
from typing import Optional, Union

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

    route_ref: Optional[RouteRefStructure] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_type: Optional[DirectionType] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_demand_type_ref_or_timeband_ref: Optional[
        Union[TimeDemandTypeRef, TimebandRef]
    ] = field(
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
    points_in_sequence: Optional[TimingPointsInJourneyPatternRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "pointsInSequence",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    points: Optional[TimingPointsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    links: Optional[TimingLinksRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
