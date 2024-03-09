from dataclasses import dataclass

from .service_exclusion_version_structure import (
    ServiceExclusionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceExclusion(ServiceExclusionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
