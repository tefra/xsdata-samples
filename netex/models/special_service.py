from dataclasses import dataclass
from .special_service_version_structure import SpecialServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SpecialService(SpecialServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
