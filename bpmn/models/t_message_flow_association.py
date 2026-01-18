from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TMessageFlowAssociation(TBaseElement):
    class Meta:
        name = "tMessageFlowAssociation"

    inner_message_flow_ref: QName | None = field(
        default=None,
        metadata={
            "name": "innerMessageFlowRef",
            "type": "Attribute",
            "required": True,
        },
    )
    outer_message_flow_ref: QName | None = field(
        default=None,
        metadata={
            "name": "outerMessageFlowRef",
            "type": "Attribute",
            "required": True,
        },
    )
