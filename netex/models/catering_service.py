from dataclasses import dataclass
from netex.models.catering_service_version_structure import CateringServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CateringService(CateringServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
