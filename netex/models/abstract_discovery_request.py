from dataclasses import dataclass
from netex.models.abstract_discovery_request_structure import AbstractDiscoveryRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractDiscoveryRequest(AbstractDiscoveryRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
