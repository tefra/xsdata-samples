from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .documentation import Documentation

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TExtension:
    class Meta:
        name = "tExtension"

    documentation: list[Documentation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    definition: None | QName = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    must_understand: bool = field(
        default=False,
        metadata={
            "name": "mustUnderstand",
            "type": "Attribute",
        },
    )
