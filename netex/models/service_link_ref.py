from dataclasses import dataclass
from netex.models.service_link_ref_structure import ServiceLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceLinkRef(ServiceLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
