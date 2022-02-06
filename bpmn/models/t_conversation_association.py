from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TConversationAssociation(TBaseElement):
    class Meta:
        name = "tConversationAssociation"

    inner_conversation_node_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "innerConversationNodeRef",
            "type": "Attribute",
            "required": True,
        }
    )
    outer_conversation_node_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "outerConversationNodeRef",
            "type": "Attribute",
            "required": True,
        }
    )
