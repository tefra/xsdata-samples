from dataclasses import dataclass
from .assistance_service_ref_structure import AssistanceServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AssistanceServiceRef(AssistanceServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
