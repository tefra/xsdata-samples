from dataclasses import dataclass
from .timing_point_in_journey_pattern_ref_structure import (
    TimingPointInJourneyPatternRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingPointInJourneyPatternRef(TimingPointInJourneyPatternRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
