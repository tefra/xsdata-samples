from dataclasses import dataclass, field
from typing import Dict, List, Optional
from .documentation import Documentation
from .extension_elements import ExtensionElements

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TBaseElementWithMixedContent:
    class Meta:
        name = "tBaseElementWithMixedContent"

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
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "documentation",
                    "type": Documentation,
                    "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
                },
                {
                    "name": "extensionElements",
                    "type": ExtensionElements,
                    "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
                },
            ),
        }
    )
