from dataclasses import dataclass
from .service_access_code_ref_structure import ServiceAccessCodeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceAccessCodeRef(ServiceAccessCodeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
