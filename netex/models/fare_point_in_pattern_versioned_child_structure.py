from dataclasses import dataclass, field
from typing import Optional

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

    scheduled_stop_point_view: Optional[ScheduledStopPointView] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    abridgement_ranking: Optional[int] = field(
        default=None,
        metadata={
            "name": "AbridgementRanking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    presentation_position: Optional[SeriesPresentationEnumeration] = field(
        default=None,
        metadata={
            "name": "PresentationPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_forbidden: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsForbidden",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    interchange_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InterchangeAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_fare_stage: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsFareStage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
