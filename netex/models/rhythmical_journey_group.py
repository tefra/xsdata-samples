from dataclasses import dataclass
from netex.models.rhythmical_journey_group_version_structure import RhythmicalJourneyGroupVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RhythmicalJourneyGroup(RhythmicalJourneyGroupVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
