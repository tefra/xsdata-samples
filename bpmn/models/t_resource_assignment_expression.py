from dataclasses import dataclass, field
from typing import Optional
from .expression import Expression
from .formal_expression import FormalExpression
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TResourceAssignmentExpression(TBaseElement):
    class Meta:
        name = "tResourceAssignmentExpression"

    formal_expression: Optional[FormalExpression] = field(
        default=None,
        metadata={
            "name": "formalExpression",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    expression: Optional[Expression] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
