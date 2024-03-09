from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .documentation import Documentation
from .extension_elements import ExtensionElements

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TBaseElement:
    class Meta:
        name = "tBaseElement"

    documentation: List[Documentation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    extension_elements: Optional[ExtensionElements] = field(
        default=None,
        metadata={
            "name": "extensionElements",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    id: Optional[str] = field(
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
