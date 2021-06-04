from dataclasses import dataclass
from netex.models.link_sequence_version_structure import LinkSequenceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPattern1(LinkSequenceVersionStructure):
    class Meta:
        name = "JourneyPattern_"
        namespace = "http://www.netex.org.uk/netex"
