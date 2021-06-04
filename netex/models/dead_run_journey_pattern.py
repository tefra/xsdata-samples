from dataclasses import dataclass
from netex.models.dead_run_journey_pattern_version_structure import DeadRunJourneyPatternVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeadRunJourneyPattern(DeadRunJourneyPatternVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
