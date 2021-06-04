from dataclasses import dataclass
from netex.models.response_structure import ResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractResponse(ResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
