from dataclasses import dataclass, field
from typing import Optional
from .t_event_definition import TEventDefinition
from .t_expression import TExpression

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TConditionalEventDefinition(TEventDefinition):
    class Meta:
        name = "tConditionalEventDefinition"

    condition: Optional[TExpression] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        }
    )
