from dataclasses import dataclass
from netex.models.link_sequence_projection_ref_structure import LinkSequenceProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkSequenceProjectionRef(LinkSequenceProjectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
