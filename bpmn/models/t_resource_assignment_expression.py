from __future__ import annotations

from dataclasses import dataclass, field

from .expression import Expression
from .formal_expression import FormalExpression
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TResourceAssignmentExpression(TBaseElement):
    class Meta:
        name = "tResourceAssignmentExpression"

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
