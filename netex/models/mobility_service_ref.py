from dataclasses import dataclass
from .mobility_service_ref_structure import MobilityServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MobilityServiceRef(MobilityServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
