from dataclasses import dataclass
from netex.models.communication_service_ref_structure import CommunicationServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CommunicationServiceRef(CommunicationServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
