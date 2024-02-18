from dataclasses import dataclass
from .section_in_sequence_versioned_child_structure import (
    LinkSequenceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkSequence(LinkSequenceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
