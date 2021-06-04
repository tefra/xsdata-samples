from dataclasses import dataclass
from netex.models.endpoint_denied_access_structure import EndpointDeniedAccessStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class EndpointDeniedAccessError(EndpointDeniedAccessStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
