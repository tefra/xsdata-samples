from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName

from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TOperation(TBaseElement):
    class Meta:
        name = "tOperation"

    in_message_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "inMessageRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        },
    )
    out_message_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "outMessageRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    error_ref: List[QName] = field(
        default_factory=list,
        metadata={
            "name": "errorRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    implementation_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "implementationRef",
            "type": "Attribute",
        },
    )
