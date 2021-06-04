from dataclasses import dataclass
from netex.models.link_sequence_version_structure import JourneyPatternVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeadRunJourneyPatternVersionStructure(JourneyPatternVersionStructure):
    class Meta:
        name = "DeadRunJourneyPattern_VersionStructure"
