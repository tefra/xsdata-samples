from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"


@dataclass
class ExtensionContentType:
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "required": True,
        }
    )
