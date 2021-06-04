from dataclasses import dataclass
from netex.models.stop_point_in_journey_pattern_ref_structure import StopPointInJourneyPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPointInJourneyPatternRef(StopPointInJourneyPatternRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
