from dataclasses import dataclass, field
from typing import Optional
from .error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class EndpointDeniedAccessStructure(ErrorCodeStructure):
    endpoint: Optional[str] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
