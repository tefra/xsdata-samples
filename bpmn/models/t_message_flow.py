from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TMessageFlow(TBaseElement):
    class Meta:
        name = "tMessageFlow"

    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    source_ref: QName = field(
        metadata={
            "name": "sourceRef",
            "type": "Attribute",
            "required": True,
        }
    )
    target_ref: QName = field(
        metadata={
            "name": "targetRef",
            "type": "Attribute",
            "required": True,
        }
    )
    message_ref: None | QName = field(
        default=None,
        metadata={
            "name": "messageRef",
            "type": "Attribute",
        },
    )
