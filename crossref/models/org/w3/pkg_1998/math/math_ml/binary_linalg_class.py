from dataclasses import dataclass, field
from typing import Dict, List, Optional

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass
class BinaryLinalgType:
    class Meta:
        name = "binary-linalg.class"
        namespace = "http://www.w3.org/1998/Math/MathML"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    xref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    encoding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    definition_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "definitionURL",
            "type": "Attribute",
        },
    )