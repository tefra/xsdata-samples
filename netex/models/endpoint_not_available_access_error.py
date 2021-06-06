from dataclasses import dataclass
from .endpoint_not_available_access_structure import EndpointNotAvailableAccessStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class EndpointNotAvailableAccessError(EndpointNotAvailableAccessStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
