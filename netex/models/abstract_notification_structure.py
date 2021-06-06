from dataclasses import dataclass
from .producer_request_endpoint_structure import ProducerRequestEndpointStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractNotificationStructure(ProducerRequestEndpointStructure):
    pass
