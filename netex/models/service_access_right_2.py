from dataclasses import dataclass
from netex.models.service_access_right_version_structure import ServiceAccessRightVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceAccessRight2(ServiceAccessRightVersionStructure):
    class Meta:
        name = "ServiceAccessRight"
        namespace = "http://www.netex.org.uk/netex"
