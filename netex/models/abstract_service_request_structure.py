from dataclasses import dataclass, field
from typing import Optional
from netex.models.abstract_request_structure import AbstractRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractServiceRequestStructure(AbstractRequestStructure):
    message_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "MessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
