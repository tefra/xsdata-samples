from dataclasses import dataclass
from .wire_link_ref_by_value_structure import WireLinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class WireLinkRefByValue(WireLinkRefByValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
