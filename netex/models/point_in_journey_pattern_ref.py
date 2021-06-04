from dataclasses import dataclass
from netex.models.point_in_journey_pattern_ref_structure import PointInJourneyPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointInJourneyPatternRef(PointInJourneyPatternRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
