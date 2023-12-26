from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from .expression import Expression
from .formal_expression import FormalExpression
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TResourceParameterBinding(TBaseElement):
    class Meta:
        name = "tResourceParameterBinding"

    formal_expression: Optional[FormalExpression] = field(
        default=None,
        metadata={
            "name": "formalExpression",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    expression: Optional[Expression] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    parameter_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "parameterRef",
            "type": "Attribute",
            "required": True,
        },
    )
