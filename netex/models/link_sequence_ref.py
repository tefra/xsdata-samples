from dataclasses import dataclass
from netex.models.link_sequence_ref_structure import LinkSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkSequenceRef(LinkSequenceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
