from dataclasses import dataclass
from netex.models.path_link_in_sequence_versioned_child_structure import PathLinkInSequenceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathLinkInSequence(PathLinkInSequenceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
