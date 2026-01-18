from dataclasses import dataclass, field

from .point_in_journey_pattern_versioned_child_structure import (
    PointInJourneyPatternVersionedChildStructure,
)
from .scheduled_stop_point_view import ScheduledStopPointView
from .series_presentation_enumeration import SeriesPresentationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FarePointInPatternVersionedChildStructure(
    PointInJourneyPatternVersionedChildStructure
):
    class Meta:
        name = "FarePointInPattern_VersionedChildStructure"

    scheduled_stop_point_view: ScheduledStopPointView | None = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    abridgement_ranking: int | None = field(
        default=None,
        metadata={
            "name": "AbridgementRanking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    presentation_position: SeriesPresentationEnumeration | None = field(
        default=None,
        metadata={
            "name": "PresentationPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_forbidden: bool | None = field(
        default=None,
        metadata={
            "name": "IsForbidden",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    interchange_allowed: bool | None = field(
        default=None,
        metadata={
            "name": "InterchangeAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_fare_stage: bool | None = field(
        default=None,
        metadata={
            "name": "IsFareStage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
