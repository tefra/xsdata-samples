from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TMessageFlowAssociation(TBaseElement):
    class Meta:
        name = "tMessageFlowAssociation"

    inner_message_flow_ref: QName = field(
        metadata={
            "name": "innerMessageFlowRef",
            "type": "Attribute",
            "required": True,
        }
    )
    outer_message_flow_ref: QName = field(
        metadata={
            "name": "outerMessageFlowRef",
            "type": "Attribute",
            "required": True,
        }
    )
