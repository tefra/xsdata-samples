from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_base_element import TBaseElement
from .t_formal_expression import TFormalExpression

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TCorrelationPropertyRetrievalExpression(TBaseElement):
    class Meta:
        name = "tCorrelationPropertyRetrievalExpression"

    message_path: TFormalExpression = field(
        metadata={
            "name": "messagePath",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        }
    )
    message_ref: QName = field(
        metadata={
            "name": "messageRef",
            "type": "Attribute",
            "required": True,
        }
    )
