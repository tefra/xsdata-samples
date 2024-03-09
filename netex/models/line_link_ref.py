from dataclasses import dataclass

from .line_link_ref_structure import LineLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LineLinkRef(LineLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
