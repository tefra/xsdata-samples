from dataclasses import dataclass
from netex.models.local_service_version_structure import LocalServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerServiceVersionStructure(LocalServiceVersionStructure):
    class Meta:
        name = "CustomerService_VersionStructure"
