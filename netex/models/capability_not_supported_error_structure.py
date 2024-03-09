from dataclasses import dataclass, field
from typing import Optional

from .error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilityNotSupportedErrorStructure(ErrorCodeStructure):
    capability_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CapabilityRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
