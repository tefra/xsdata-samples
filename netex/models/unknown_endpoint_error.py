from dataclasses import dataclass
from .unknown_endpoint_error_structure import UnknownEndpointErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownEndpointError(UnknownEndpointErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
