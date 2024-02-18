from dataclasses import dataclass
from .link_in_link_sequence_versioned_child_structure import (
    LinkInLinkSequenceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkInLinkSequence(LinkInLinkSequenceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
