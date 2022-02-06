from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from .t_base_element import TBaseElement
from .t_formal_expression import TFormalExpression

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TCorrelationPropertyRetrievalExpression(TBaseElement):
    class Meta:
        name = "tCorrelationPropertyRetrievalExpression"

    message_path: Optional[TFormalExpression] = field(
        default=None,
        metadata={
            "name": "messagePath",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        }
    )
    message_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "messageRef",
            "type": "Attribute",
            "required": True,
        }
    )
