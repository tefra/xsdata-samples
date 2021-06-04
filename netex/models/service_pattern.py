from dataclasses import dataclass
from netex.models.service_pattern_version_structure import ServicePatternVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServicePattern(ServicePatternVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
