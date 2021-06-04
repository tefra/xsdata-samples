from dataclasses import dataclass
from netex.models.abstract_service_request_structure import AbstractServiceRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractServiceRequest(AbstractServiceRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
