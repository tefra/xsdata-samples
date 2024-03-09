from dataclasses import dataclass

from .stop_point_in_journey_pattern_versioned_child_structure import (
    StopPointInJourneyPatternVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPointInJourneyPattern(
    StopPointInJourneyPatternVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
