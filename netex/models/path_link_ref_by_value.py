from dataclasses import dataclass
from .path_link_ref_by_value_structure import PathLinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathLinkRefByValue(PathLinkRefByValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
