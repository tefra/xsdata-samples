from dataclasses import dataclass
from netex.models.network_ref_structure import NetworkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NetworkRef(NetworkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
