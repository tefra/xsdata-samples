from dataclasses import dataclass
from .section_in_sequence_versioned_child_structure import JourneyPatternVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeadRunJourneyPatternVersionStructure(JourneyPatternVersionStructure):
    class Meta:
        name = "DeadRunJourneyPattern_VersionStructure"
