from __future__ import annotations

from dataclasses import dataclass, field

from .documentation import Documentation
from .extension_elements import ExtensionElements

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
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
    extension_elements: None | ExtensionElements = field(
        default=None,
        metadata={
            "name": "extensionElements",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    id: None | str = field(
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
