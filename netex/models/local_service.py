from dataclasses import dataclass
from netex.models.local_service_version_structure import LocalServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LocalService(LocalServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
