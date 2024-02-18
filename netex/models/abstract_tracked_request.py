from dataclasses import dataclass
from .request_structure import RequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractTrackedRequest(RequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
