from dataclasses import dataclass
from netex.models.timing_point_in_journey_pattern_versioned_child_structure import TimingPointInJourneyPatternVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingPointInJourneyPattern(TimingPointInJourneyPatternVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
