from dataclasses import dataclass, field
from typing import Optional

from .documentation import Documentation
from .extension_elements import ExtensionElements

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TBaseElement:
    class Meta:
        name = "tBaseElement"

    documentation: list[Documentation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    extension_elements: ExtensionElements | None = field(
        default=None,
        metadata={
            "name": "extensionElements",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
