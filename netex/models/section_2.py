from dataclasses import dataclass
from .link_sequence_version_structure import LinkSequenceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Section2(LinkSequenceVersionStructure):
    class Meta:
        name = "Section_"
        namespace = "http://www.netex.org.uk/netex"
