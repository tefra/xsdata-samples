from dataclasses import dataclass
from .capabilities_request_structure import CapabilitiesRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilitiesRequest(CapabilitiesRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
