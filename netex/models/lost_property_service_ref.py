from dataclasses import dataclass
from .lost_property_service_ref_structure import LostPropertyServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LostPropertyServiceRef(LostPropertyServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
