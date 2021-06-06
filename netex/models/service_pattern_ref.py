from dataclasses import dataclass
from .service_pattern_ref_structure import ServicePatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServicePatternRef(ServicePatternRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
