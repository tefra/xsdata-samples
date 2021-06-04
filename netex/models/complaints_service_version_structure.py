from dataclasses import dataclass
from netex.models.customer_service_version_structure import CustomerServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ComplaintsServiceVersionStructure(CustomerServiceVersionStructure):
    class Meta:
        name = "ComplaintsService_VersionStructure"
