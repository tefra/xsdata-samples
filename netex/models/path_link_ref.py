from dataclasses import dataclass

from .path_link_ref_structure import PathLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathLinkRef(PathLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
