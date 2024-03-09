from dataclasses import dataclass

from .capabilities_response_structure import CapabilitiesResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilitiesResponse(CapabilitiesResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
