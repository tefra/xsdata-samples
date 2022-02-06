from dataclasses import dataclass, field
from typing import Dict, List, Optional

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DI"


@dataclass
class DiagramElement:
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DI"

    extension: Optional["DiagramElement.Extension"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )

    @dataclass
    class Extension:
        other_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
            }
        )
