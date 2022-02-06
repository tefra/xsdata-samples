from dataclasses import dataclass, field
from typing import Optional
from .t_base_element import TBaseElement
from .t_formal_expression import TFormalExpression
from .t_implicit_throw_event import TImplicitThrowEvent

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TComplexBehaviorDefinition(TBaseElement):
    class Meta:
        name = "tComplexBehaviorDefinition"

    condition: Optional[TFormalExpression] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        }
    )
    event: Optional[TImplicitThrowEvent] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
