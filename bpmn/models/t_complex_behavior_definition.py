from __future__ import annotations

from dataclasses import dataclass, field

from .t_base_element import TBaseElement
from .t_formal_expression import TFormalExpression
from .t_implicit_throw_event import TImplicitThrowEvent

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TComplexBehaviorDefinition(TBaseElement):
    class Meta:
        name = "tComplexBehaviorDefinition"

    condition: TFormalExpression = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        }
    )
    event: None | TImplicitThrowEvent = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
