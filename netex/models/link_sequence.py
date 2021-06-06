from dataclasses import dataclass
from .link_sequence_version_structure import LinkSequenceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkSequence(LinkSequenceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
