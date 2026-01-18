from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .expression import Expression
from .formal_expression import FormalExpression
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TResourceParameterBinding(TBaseElement):
    class Meta:
        name = "tResourceParameterBinding"

    formal_expression: None | FormalExpression = field(
        default=None,
        metadata={
            "name": "formalExpression",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    expression: None | Expression = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    parameter_ref: QName = field(
        metadata={
            "name": "parameterRef",
            "type": "Attribute",
            "required": True,
        }
    )
