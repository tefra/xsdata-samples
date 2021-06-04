from dataclasses import dataclass, field
from typing import Optional
from netex.models.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnapprovedKeyAccessStructure(ErrorCodeStructure):
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
