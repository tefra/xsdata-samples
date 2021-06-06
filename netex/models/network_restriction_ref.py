from dataclasses import dataclass
from .network_restriction_ref_structure import NetworkRestrictionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NetworkRestrictionRef(NetworkRestrictionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
