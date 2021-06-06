from dataclasses import dataclass
from .wire_junction_version_structure import WireJunctionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class WireJunction(WireJunctionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
