from dataclasses import dataclass
from netex.models.service_exclusion_ref_structure import ServiceExclusionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceExclusionRef(ServiceExclusionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
