from dataclasses import dataclass
from netex.models.link_ref_structure import LinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkRef(LinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
