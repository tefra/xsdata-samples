from dataclasses import dataclass
from netex.models.communication_service_version_structure import CommunicationServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CommunicationService(CommunicationServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
