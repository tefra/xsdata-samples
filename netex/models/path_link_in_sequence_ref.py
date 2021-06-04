from dataclasses import dataclass
from netex.models.path_link_in_sequence_ref_structure import PathLinkInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathLinkInSequenceRef(PathLinkInSequenceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
