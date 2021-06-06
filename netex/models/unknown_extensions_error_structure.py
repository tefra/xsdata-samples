from dataclasses import dataclass, field
from typing import List
from .error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownExtensionsErrorStructure(ErrorCodeStructure):
    extension_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
