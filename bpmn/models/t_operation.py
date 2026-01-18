from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TOperation(TBaseElement):
    class Meta:
        name = "tOperation"

    in_message_ref: QName = field(
        metadata={
            "name": "inMessageRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        }
    )
    out_message_ref: None | QName = field(
        default=None,
        metadata={
            "name": "outMessageRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    error_ref: list[QName] = field(
        default_factory=list,
        metadata={
            "name": "errorRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    implementation_ref: None | QName = field(
        default=None,
        metadata={
            "name": "implementationRef",
            "type": "Attribute",
        },
    )
