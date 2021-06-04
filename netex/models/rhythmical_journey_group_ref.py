from dataclasses import dataclass
from netex.models.rhythmical_journey_group_ref_structure import RhythmicalJourneyGroupRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RhythmicalJourneyGroupRef(RhythmicalJourneyGroupRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
