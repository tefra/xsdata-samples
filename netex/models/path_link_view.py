from dataclasses import dataclass
from .path_link_derived_view_structure import PathLinkDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathLinkView(PathLinkDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
