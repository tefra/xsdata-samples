from dataclasses import dataclass

from .hire_service_version_structure import HireServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class HireService(HireServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
