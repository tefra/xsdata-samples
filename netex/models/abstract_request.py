from dataclasses import dataclass

from .abstract_request_structure import AbstractRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractRequest(AbstractRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
