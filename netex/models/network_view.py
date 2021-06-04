from dataclasses import dataclass
from netex.models.network_derived_view_structure import NetworkDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NetworkView(NetworkDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
