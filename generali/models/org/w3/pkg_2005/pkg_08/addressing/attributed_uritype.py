from dataclasses import dataclass, field
from typing import Dict

__NAMESPACE__ = "http://www.w3.org/2005/08/addressing"


@dataclass
class AttributedUritype:
    class Meta:
        name = "AttributedURIType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
