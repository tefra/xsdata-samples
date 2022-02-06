from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TMessageFlow(TBaseElement):
    class Meta:
        name = "tMessageFlow"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    source_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "sourceRef",
            "type": "Attribute",
            "required": True,
        }
    )
    target_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "targetRef",
            "type": "Attribute",
            "required": True,
        }
    )
    message_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "messageRef",
            "type": "Attribute",
        }
    )
