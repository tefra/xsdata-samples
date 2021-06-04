from dataclasses import dataclass
from netex.models.wire_link_ref_structure import WireLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class WireLinkRef(WireLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
