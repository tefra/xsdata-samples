from dataclasses import dataclass

from .assistance_service_version_structure import (
    AssistanceServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AssistanceService(AssistanceServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
