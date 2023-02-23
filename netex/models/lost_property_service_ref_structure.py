from dataclasses import dataclass
from .local_service_ref_structure import LocalServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LostPropertyServiceRefStructure(LocalServiceRefStructure):
    pass
