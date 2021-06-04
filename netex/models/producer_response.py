from dataclasses import dataclass
from netex.models.producer_response_structure import ProducerResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ProducerResponse(ProducerResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
