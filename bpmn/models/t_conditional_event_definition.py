from __future__ import annotations

from dataclasses import dataclass, field

from .t_event_definition import TEventDefinition
from .t_expression import TExpression

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TConditionalEventDefinition(TEventDefinition):
    class Meta:
        name = "tConditionalEventDefinition"

    condition: TExpression = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        }
    )
